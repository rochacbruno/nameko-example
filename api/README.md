# get the code

If you did not cloned yet do it now!

```bash
$ git clone https://github.com/rochacbruno/nameko-example
````

# running the API


1. Create a virtual environment
   You need vitualenv and virtualenvwrapper installed

```bash
$ mkvirtualenv api
$ workon api
(api)$ cd nameko-example/api
(api)$ pip install -r requirements.txt
(api)$ manage run
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Access [http://localhost:5000](http://localhost:5000) to see it in action.

Play with API and see the logs being printed in the service shell or the email being sent.


If you need to change port and host use:

```bash
(api)$ manage run --port=8080 --host=192.168.0.1 --debug --use_reloader
```

