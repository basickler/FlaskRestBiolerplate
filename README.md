# Flask REST Service Boilerplate

Losely based on a [free codecamp page]("https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/#project-setup-and-organization")

You can find the code for that [here](https://github.com/cosmic-byte/flask-restplus-boilerplate)

I've modified the structure a little bit "lot" to fit our needs.

# Production
To run using gunicorn 
```shell script
venv/bin/gunicorn app
```

To use one of the configs
```shell script
venv/bin/gunicorn --config gunicorn_config.py app
```

To start on a custom port (say from docker :P). Note command line takes precidence over config file.
```shell script
venv/bin/gunicorn --config gunicorn_config.py --bind 0.0.0.0:10086 app
```


# Testing and Dev
To run using flask
```shell script
python3 manage.py run
```
 
 To run testing scripts (not implemented by default)
 ```shell script
python3 manage.py test
```

Using the manage.py framework you can do things like autoinit db connections and the like.