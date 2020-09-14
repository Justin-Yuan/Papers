# Docker

---

# Resources

youtube link 1:  

[Learn Docker in 12 Minutes 🐳](https://www.youtube.com/watch?v=YFl2mCHdv24&list=PLpmzFAo4EHLvMvd1A9w3tnLqUHazF7FQ9&index=4&t=0s)

youtube link 2:

[Docker Compose in 12 Minutes](https://www.youtube.com/watch?v=Qw9zlE3t8Ko&list=PLpmzFAo4EHLvMvd1A9w3tnLqUHazF7FQ9&index=2)

youtube link 3: 

[Deploy Docker Containers with Docker Cloud](https://www.youtube.com/watch?v=F82K07NmRpk)

---

# Intro to Docker

- virtual machine v.s. containers
- containers are faster, use fewer resources and memory

    ![Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_8.58.26_PM.png](Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_8.58.26_PM.png)

- container is a running instance of an image, an image is a template for creating the environment, a snapshot of the environment at some time
- image contains OS, software and application code
- image is defined in a Dockerfile

    ![Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.01.33_PM.png](Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.01.33_PM.png)

- find existing images on Docker Hub
- define base image using FROM keyword, with <image name>:<tag>

```docker
FROM php:7.0-apache
```

- keywords
    - COPY
    - EXPOSE, expose port in container
- build docker image

```docker
docker build -t <image name> <output location>
```

- run image
    - can do port forwarding with -p 80:80

```docker
docker run <image name>
```

- but buidling an image will make copy of source files, so updates to source files will not be reflected
    - can mount a local folder as volume in container to grab changes, use -v <source folder>:<target folder>
    - useful for development but still need to rebuild when deploying
- have 1 process per container

---

# Docker-compose

- applications as micro-srevices, website calls application by its API

    ![Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.22.51_PM.png](Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.22.51_PM.png)

    ![Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.24.51_PM.png](Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.24.51_PM.png)

- keywords
    - CMD, run a shell command (optinally with arguments), e.g.

    ```docker
    CMD ["python", "api.py"]
    ```

- docker compose allows to run all services in a configuration file, use 1 command to spin up all the containers we need
    - docker-compose.yml

        ![Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.39.02_PM.png](Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.39.02_PM.png)

    - run with (in the same folder as yaml file)

    ```docker
    docker-compose up 
    ```

    - docker compose creates a virtual network for the containers, so each container can see the others, and each with host name matching its service name in yaml file
    - docker compose detach mode with -d, so it runs in the background
    - to see all processes running under docker, use

    ```docker
    docker ps 
    ```

    - to step running docker process, fore-ground use ctrl-c, background use

    ```docker
    docker stop 
    ```

---

# Cloud Deployment

- deploy containers with Docker Cloud

    ![Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.45.23_PM.png](Docker%20151edbc8ce904b5aa5ab28883fca8819/Screen_Shot_2020-07-15_at_9.45.23_PM.png)

- Docker Cloud
    - nodes are servers to run your containers
    - nodes can be grouped into node clusters
    - services are abstractions to containers
        - when you start the service, docker cloud will spin up the docker container in the background
    - stacks are like docker compose, let you define services in a yaml file
- Docker Hub
    - host repositories to host images
    - can use others, e.g. Github, Gitlab, Bitbucket, etc
- endpoints will specify the URL in which your services are hosted

---