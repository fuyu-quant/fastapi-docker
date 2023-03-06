# fastapi-docker
<img src="image/FastAPI.png" width="400">
FastAPI dokcer

## Contents
* [Basic docker operations](#basic-docker-operations)
    * [Basic docker commands](#basic-docker-commands)
    * [How to run the Dockerfile](#how-to-run-the-dockerfile)
* [Dockerfiles](#dockerfiles)

## Basic docker operations
### Basic docker commands
```Dockerfile
# Enter the container
docker-compose exec Docker-service-name bash

# Docker image list
docker images

# Remove docker image
dokcer rmi Image-name

# Check active containers
docker ps -a

# Docker network list
docker network ls

# Details of any docker network
docker network inspect Network-name

# Container to container http communication
# container name : Container name for communication destination
# port : Open ports of the container to which you are communicating
curl http://[container name]:[port]/
# example
curl http://fastapi:8040/
```


### How to run the Dockerfile
How to start a dockerfile using Docker compose
```bash
# Start container
bash docker.sh up

# Rebuild the docker image and start container
bash docker.sh force

# Stop container
bash docker.sh down

# Stop the container and delete the image
bash docker.sh rm 
```

## FastAPI
Execution command
```bash
docker-compose exec fastapi bash
cd src
uvicorn main:app --reload  --host 0.0.0.0 --port 8040
```
* Link  
    * http://0.0.0.0:8040/
    * http://127.0.0.1:8040/docs
    * http://127.0.0.1:8040/redoc
* Reference  
    * https://buildersbox.corp-sansan.com/entry/tech18_container  
    * https://qiita.com/Brutus/items/3133766e14f11d269933

## Reference