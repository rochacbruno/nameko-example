import yagmail
from nameko.rpc import rpc, RpcProxy
from dynaconf import settings


if settings.DEBUG:
    print('Starting in DEBUG mode')
else:
    print('Starting in PRODUCTION mode')


class Mail(object):
    name = "mail"

    @rpc
    def send(self, to, subject, contents):
        if settings.DEBUG:
            print(
                u'Sending email "%s" to "%s" with contents "%s"' %
                (subject, to, contents)
            )
            return

        # email will be sent only if DEBUG=False in settings.py
        # or you do:
        #  export DYNACONF_DEBUG='@bool False'
        yag = yagmail.SMTP(settings.EMAIL, settings.PASSWORD)

        # Tip: export DYNACONF_EMAIL='myemail@gmail.com'
        #      export DYNACONF_PASSWORD='secret'
        yag.send(cc=to.encode('utf-8'),
                 subject=subject.encode('utf-8'),
                 contents=[contents.encode('utf-8')])


class Compute(object):
    name = "compute"
    mail = RpcProxy('mail')

    @rpc
    def compute(self, operation, value, other, email):
        operations = {u'sum': lambda x, y: int(x) + int(y),
                      u'mul': lambda x, y: int(x) * int(y),
                      u'div': lambda x, y: int(x) / int(y),
                      u'sub': lambda x, y: int(x) - int(y)}
        try:
            result = operations[operation](value, other)
        except Exception as e:
            self.mail.send.async(email, "An error occurred", str(e))
            raise
        else:
            self.mail.send.async(
                email,
                "Your operation is complete!",
                "The result is: %s" % result
            )
            return result