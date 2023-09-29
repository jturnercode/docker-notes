# nginx-unit & plotly

Docker example that uses nginx unit with plotly

## included

- Dockerfile
- requirements.txt
- config.json (nginx-unit configuration)
- python code

## important

It is important to understand how the nginx-unit .config file points the server to the python app.
At a high level the applications section in the json below specifies type of application that nginx-unit will serve, source code location, and callable that unit runs as the app.

For more details and settings go to [nginx-unit configuation](https://unit.nginx.org/configuration/) section.

In below example, we run a python 3 application named `app.py` located on server directory `/www/`. Unit looks for callable named `server` in the `app.py` file to run code. Per below, Unit will listen on any host IP with specified port 8000 and pass request to application at location applications/webapp in json.

```
{
    "listeners":{
        "*:8000":{
            "pass":"applications/webapp"
        }
    },

    "applications":{
        "webapp":{
            "type":"python 3",
            "path":"/www/",
            "module": "app",
            "callable": "server"
        }
    }
}
```

## docker commands

```
docker build --tag=unit-webapp .
```

To create and run container:

```
docker run --rm --env-file .tmp-env -it -p 8080:8000 unit-webapp
```

> **NOTE:**  
> `--rm` flag causes all containers to be deleted if closed. Replace with -d and remove -it when ready to deploy.

_Alternative:_
Using `--mount type=bind` to persist data on host machine by mounting directories to container.  
In Dockerfile comment out line 10 & 11 to run container with below commands:

```
export UNIT=$(                                                         \
      docker run --rm -it  --env-file .tmp-env                    \
      --mount type=bind,src="$(pwd)/config/",dst=/docker-entrypoint.d/   \
      --mount type=bind,src="$(pwd)/log/unit.log",dst=/var/log/unit.log  \
      --mount type=bind,src="$(pwd)/state",dst=/var/lib/unit             \
      --mount type=bind,src="$(pwd)/webapp",dst=/www                     \
      -p 8080:8000 unit-webapp                                           \
  )
```
