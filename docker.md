# docker

## docker documentation

- [get started](https://docs.docker.com/get-started/)
- [python guide](https://docs.docker.com/language/python/)
- [docker run](https://docs.docker.com/engine/reference/run/)

## [Dockerfile](https://docs.docker.com/engine/reference/builder/)

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.

Set of instructions to build an image

### format

```
# Comment
INSTRUCTION arguments
```

Docker treats lines that begin with `#` as a comment.

## image

### list images

```
docker image ls
```

> REPOSITORY TAG IMAGE ID CREATED SIZE  
> fasttest latest 7a7d11b2ac20 5 hours ago 1.04GB  
> dpage/pgadmin4 latest 6496b01fd1c2 3 months ago 526MB  
> postgres 14.8-alpine b508d2f01950 3 months ago 235MB

### pull image

Download a docker image from hub.docker.com

```
docker image pull <image_name>:<image_version/tag>
```

## docker build

The `docker build` command builds Docker images from a `Dockerfile` and a "context". A build's context is the set of files located in the specified `PATH` or `URL`. The build process can refer to any of the files in the context. For example, your build can use a `COPY` instruction to reference a file in the context.

The `URL` parameter can refer to three kinds of resources: Git repositories, pre-packaged tarball contexts and plain text files.

_By default the `docker build` command will look for a `Dockerfile` at the root of the build context. `-f` can be used to specify alternate route to file._

```
docker build [OPTIONS] PATH | URL | -
```

Typical usage:

```
docker build --tag <tag_name> .
```

> NOTE: The _dot(.)_ in the command specifies to the Docker daemon to use the shell’s current working directory

[Options:](https://docs.docker.com/engine/reference/commandline/build/#options)

- --tag [-t] Name and optionally a tag in the name:tag format
- --file [-f] Name of the Dockerfile (Default is PATH/Dockerfile)

See other options [here](https://docs.docker.com/engine/reference/commandline/build/#options)

## docker run

### usage

Create and run a new container from an image

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

common options:

- --name (Assign a name to the container)
- --volume [-v] (Bind mount a volume)
- --publish [-p] (Publish a container's port(s) to the host)
- --expose (Expose a port or a range of ports)
- --workdir [-w] (Working directory _inside the container_)
- --rm (Automatically remove the container when it exits)
- -tty [-t] (Allocate a pseudo-TTY, ie. terminal)
- --mount (Attach a filesystem mount to the container)
- --ip (IPv4 address)
- --interactive [-i] (Keep STDIN open even if not attached)
- --detach [-d] (Run container in background and print container ID)

see all options [here](https://docs.docker.com/engine/reference/commandline/run/)

example:

```
docker run --name <container_name> -it debian
```

This example runs a container named test using the debian:latest image. The -it instructs Docker to allocate a pseudo-TTY connected to the container's stdin; creating an interactive bash shell in the container.

### detach

in docker run command, means that a Docker container runs in the background of your terminal. _It does not receive input or display output._ **Using detached mode also allows you to close the opened terminal session without stopping the container.**

```
docker run -d --name <container_name> <image_name>
```

### publish port

Publish allows to map a container’s port or a range of ports to the host explicitly.

So, while it’s possible for your Docker containers to connect to the outside world without making any changes to your code, it’s not possible for the outside world to connect to your Docker containers.

Publishing ports produce a firewall rule that binds a container port to a port on the Docker host, ensuring the ports are accessible to any client that can communicate with the host.

using cmd:

```
docker run  -p <host_port>:<container_port> --name <container_Name> <image_name>
```

Below binds container's TCP port to host's port 8080 for connections to host IP 192.0.2.1. **By default, Docker binds published container ports to the 0.0.0.0 IP address, which matches any IP address on the system.** You can also specify udp and sctp ports.

```
docker run -p 192.0.2.1:8080:80/tcp <imagename>
```

### expose

By default, the EXPOSE instruction does not expose the container’s ports to be accessible from the _host_. In other words, it only makes the stated ports available for inter-container interaction.

For example, let’s say you have a Node.js application and a Redis server deployed on the same Docker network. To ensure the Node.js application communicates with the Redis server, the Redis container should expose a port.

```
docker run --expose=8000 <imagename>
```

In dockerfile:

```
EXPOSE 8080/udp
EXPOSE 8080/tcp
```

Above specifies both UDP and TCP. default is tcp

## containers

### list containers

```
docker ps [OPTIONS]
```

common options:

- -a (show all containers, default only shows running containers)
- -s (display total file size)
- --last n (show last `n` created containers, includes all states)

### start container

```
docker start <container_id>
```

### stop container

```
docker stop <container_id>
```

### remove container

```
docker rm <container_id>
```

### login to container

starts a terminal inside container. This only worked for me on windows cmd (did not work on git bash prompt).

```
docker exec -it <container_name> /bin/bash
```

## volumes

### create volume

Creates a new volume that containers can consume and store data in. If a name is not specified, Docker generates a random name.

```
docker volume create [OPTIONS] [VOLUME]
```

Example:

```
$ docker volume create hello
$ docker run -d -v hello:/world busybox ls /world
```

The first line creates a volume with name _hello_.

The mount is between the _hello_ volume (on host machine) is created inside the container's /world directory. Docker does not support relative paths for mount points inside the container.

> **IMPORTANT!  
> In Windows, the volumes are saved on WSL (Windows Subsystem for Linux) file system.**  
> To access type `\\wsl$` in windows explorer and navigate to directory where volume is located.  
> Docker volumes typ located at `\\wsl$\docker-desktop-data\data\docker\volumes`

Multiple containers can use the same volume in the same time period. This is useful if two containers need access to shared data.

> NOTE: Volume names must be unique among drivers.

### named volume

Create a container with a named volume which is mounted to specified <container_directory> on the container.

```
docker run -it --name <container_name> -v <named_volume>:<container_directory> <image_name> /bin/bash
```

> Note: `/bin/bash` starts bash inside container, this is optional command.  
> Run from cmd prompt in windows.

example creates a new volume named `ngvol` and then mounts to container directory `/appdata`.

```
docker volume create ngvol
docker run -it --name ngcontainer -v ngvol:/appdata nginx /bin/bash
```

> NOTE: `docker volume create ngvol` is not technically needed. Running docker run with -v will create volume if it does not exist.

### host volume

Save data on host machine. Unlike creating a volume, this option saves directly on file system, no 'volume' is create.

Example saves data on C: drive on windows machine.

```
mkdir C:\foo2
docker run -it --name ngcontainer2 -v C:\foo2:\appdata nginx /bin/bash
```

### anonymous volume

Create a container with an anonymous volume (noted by rndom hash when running `docker volume ls`) which is mounted as `-v <volume_name>` on container. On host system it maps to a random-hash directory under `/var/lib/docker`(linux) directory.

In example below, a anonymous volume with random hash is created and mounted to container created directory _/data01_.

```
docker run -it --name <container_name> -v /data01 nginx /bin/bash
```

> _Using anonymous volumes is not good practive as it is hard to determine which container is using a volume._

### list volume

```
docker volume ls
```

### inspect a volume

```
docker volume inspect <volume_name>
```

> REMINDER: _In windows the volumes are saved in WSL. See note under [create volume](#create-volume) section._

### remove volume

Remove one or more volumes. You cannot remove a volume that is in use by a container.

```
docker volume rm [OPTIONS] <volumename>
```
