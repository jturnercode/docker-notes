# Python image
FROM python:3.10-slim

WORKDIR ./app

# install python library dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy files to container ./app directory
COPY ./app/* .


# Run app by uncommenting CMD line for
# specific plotly dash (graph.py, app.py, or flask-main.py)
# the port specified for gunicorn in dockerfile CMD
# should match docker <container-port> that is binded
# to <host-port> per `docker build -p <host-port>: <container-port>`

# run container with graph.py
# CMD ["gunicorn", "-b", "0.0.0.0:8081", "graph:server"]

# Run container with app.py
# CMD ["gunicorn", "-b", "0.0.0.0:8082", "app:server"]

# run container with main.py (flask app)
# CMD ["gunicorn", "-b", "0.0.0.0:8083", "flask-main:app"]

# run multiple commands, ie servers on container
CMD gunicorn -b 0.0.0.0:8081 graph:server & gunicorn -b 0.0.0.0:8082 app:server


# Other gunicorn commands
# - D (detach server)
# --env (environmental variable, see https://docs.gunicorn.org/en/stable/settings.html#raw-env)

# docker commands to test dockerfile
# docker build -t <img-name>
# docker run -it --rm -p 8081:8081 -p 8083:8083 <img-name>