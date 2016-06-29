# get the code

If you did not cloned yet do it now!

```bash
$ git clone https://github.com/rochacbruno/nameko-example
````

# running the nameko service

1. Install **docker** and get a local rabbit

```bash
$ docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

Check if rabbit is running
```bash
$ docker ps
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS              PORTS                                                                                        NAMES
441f002d2a77        rabbitmq:3-management   "/docker-entrypoint.s"   12 minutes ago      Up 12 minutes       4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp, 15671/tcp, 25672/tcp, 0.0.0.0:15672->15672/tcp   some-rabbit

```

also you can do by going to the browser and accessing http://localhost:15672 using credentials guest:guest if you can login to RabbitMQ dashboard it means you have it running locally for development.


2. Create a virtual environment
   You need vitualenv and virtualenvwrapper installed

```bash
$ mkvirtualenv nameko_service
(nameko_service)$ cd nameko-example/service
(nameko_service)$ pip install -r requirements.txt
(nameko_service)$ nameko run service --broker amqp://guest:guest@localhost
or use '$ make run'

Starting in DEBUG mode
starting services: mail, compute
Connected to amqp://guest:**@127.0.0.1:5672//
Connected to amqp://guest:**@127.0.0.1:5672//
< use CTRL+C to stop >
```

> Emails will not be sent, just printed out in console, to actually send emails follow next steps.


# Sending real emails

service starts in DEBUG mode, if you want to send emails:

1. Check if your gmail account is allowing external services to send emails (in account config)
2. Change variables in `settings.py` file or export as:

```bash
export DYNACONF_DEBUG='@bool False'
export DYNACONF_EMAIL='myemail@gmail.com'
export DYNACONG_PASSWORD='secret_password'
```

then

```bash
$ workon nameko_service
(nameko_service)$ cd nameko-example/service
(nameko_service)$ pip install -r requirements.txt
(nameko_service)$ nameko run service --broker amqp://guest:guest@localhost
or use '$ make run'

Starting in PRODUCTION mode
starting services: mail, compute
Connected to amqp://guest:**@127.0.0.1:5672//
Connected to amqp://guest:**@127.0.0.1:5672//
```

Leave this shell running and go the [**api**](../api/README.md) in another shell!