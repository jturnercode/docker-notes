# nginx unit static files example

Docker example nginx unit

## contents

- Dockerfile
- Nginx Unit config.json
- web folder
  - arrow images
  - index.html
  - main.js
  - styles.css

## usage

> **Note**  
> Docker desktop or similar should be installed on host machine to run this example.

1. Clone the `unit-static` folder and contents to host machine.
2. cd into `unit-static` folder
3. from command prompt run below to build docker img

```
docker build -t unit-static-img .
```

4. run below to run container

```
docker run -it --rm --name static-cont -p 8080:80 unit-static-img
```

docker container should run with no errors, goto `localhost:8080` to see static webpage with javascript, css, and images.

## todo

- add more html
- add another page and use routes
