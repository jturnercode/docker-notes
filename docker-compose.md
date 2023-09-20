# docker-compose

## docker-compose.yaml

The `docker-compose.yaml` file holds instruction to build multi-container applications.

.yaml files rely on indetation.

Below is an example `docker-compose.yaml`:

```
version: "3.8"
services:
  postgres:
    image: postgres:14.8-alpine
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
  pgadmin:
    image: dpage/pgadmin4
    restart: always
    ports:
      - "5050:80"
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@pgadmin.com
      PGADMIN_DEFAULT_PASSWORD: mypgadminpass
    volumes:
      - pgadmin_data:/var/lib/pgadmin
    depends_on:
      - postgres


```

- **version**: specifies docker-compose version, note that wrapped in quotes.
- **services**: Define the two services Docker needs to run, “postgres” and “pgadmin.”
- **image**: Specifies the Docker Hub images that will be downloaded and used for our services. We don’t apply a tag for them since we want to use the most recent versions. However, if you need a specific one, you can look at the available for PostgreSQL and pgAdmin and use it, specifying it as, for example, “postgres:15.2-alpine.”
- **restart**: Configure the Docker container always to restart if it stops unexpectedly.
- **ports**: Map the TCP port on your host machine to the container port. This way, the containerized service is exposed outside the container and can be accessed remotely.
- **environment**: Set environment variables for application authentication and setup. Be sure to change the values of the “POSTGRES_PASSWORD” environment for the PostgreSQL’s “postgres” admin user and pgAdmin (“PGADMIN_DEFAULT_EMAIL” and “PGADMIN_DEFAULT_PASSWORD“) to what you want.
- **volumes**: Mount named Docker volumes for application files to persist your data. Otherwise, the data will be lost when the container restarts.
- **depends_on**: Allows you to run services in order. In our case, the “pgadmin” service will not start until “postgres” is not up and running.

## compose up & down

Build containers per `docker-compose.yaml` instructions. Run below:

```
docker-compose up [OPTIONS]
```

- -d (detach)

`docker-compose down` stops and removes containers and networks created previously by the `docker-compose up`

```
docker-compose down
```

To stop and remove containers alongside their associated Docker images:

```
docker-compose down --rmi all
```

To delete permanently stored data in the Docker volumes:

```
docker-compose down -v
```

## essential commands

To view a list of all the containers that are currently running in your deployment, type:

```
docker-compose ps
```

To stop all docker containers that are running in the background, use the command as shown below:

```
docker-compose stop
```

To only one of the containers, not all of them. Run `docker-compose stop` followed by the service name defined in the `docker-compose.yaml` file. Notice not the container name but the service name.

```
docker-compose stop <service-name>
```

From your project directory, start up your application by running:

```
docker-compose stop
```

## logs

The `docker-compose logs` command displays log output from services.

```
docker-compose logs <service-name>
```

To aggregate the logs of every container in your stack and track what’s happening in them in real-time, type:

```
docker-compose logs -f
```
