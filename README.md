# FCN_project

## Deploy front end

1. create .env for production
``` VERSION=RELEASE python genenv.py ```

2. build docker image
``` docker build -t {registry-name}/fcn-frontend frontend/. ```

3. push docker image
``` docker push {registry-name}/fcn-frontend ```

- go to remote server

4. pull docker image from remote server
``` docker pull {registry-name}/fcn-frontend ```

5. stop and remove old container
``` docker stop fcn-frontend && docker rm fcn-frontend ```

6. docker run
``` docker run --name fcn-frontend --restart=always --network fcn_network -p 3000:3000 -d {registry-name}/fcn-frontend ```

## Deploy back end

1. build docker image
``` docker build -f Dockerfile.app -t {registry-name}/fcn-api . ```

2. push docker image
``` docker push {registry-name}/fcn-api ```

- go to remote server

3. pull docker image from remote server
``` docker pull {registry-name}/fcn-api ```

4. stop and remove old container
``` docker stop fcn-api && docker rm fcn-api ```

5. docker run
``` docker run --name fcn-api --restart=always --network fcn_network -p 8000:8000 -d {registry-name}/fcn-api ```