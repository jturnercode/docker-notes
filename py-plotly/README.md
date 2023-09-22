# python plotly docker

Docker example using python

## contents

- Dockerfile
- requirements.txt
- app folder with python code

## usage

> Docker desktop or similar should be installed on machine to run this example.

1. Clone the `py-plotly` folder and contents to host machine.
2. cd into `py-plotly` folder
3. from command prompt run below to build docker img

```
docker build -t py-plotly-img
```

4. run below to run container

```
docker run -it --rm --name plotly-cont -p 8081:8081 -p 8082:8082 py-plotly-img
```

docker container should run with no errors, goto `localhost:8081` or `localhost:8081` to see plotly dashboards.
