pip3 install --target=. -r ../requirements.txt --no-user




docker run --name lambdalayer --rm --env HTTP_PROXY --env HTTPS_PROXY --env NO_PROXY --mount type=bind,source="$(pwd)"/lambda_packages,target=/var/task/lambdalayer -it aws-python3.9:local bash

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker system prune --volumes

docker pull amazonlinux:latest

docker run -it amazonlinux:latest bash

docker run --name lambdalayer --rm --env HTTP_PROXY --env HTTPS_PROXY --env NO_PROXY --mount type=bind,source=//c/Github/hrs-swagger-repo/lambda_packages,target=/var/task/lambdalayer -it amazonlinux:latest bash

docker run -it --volume //c/Github/hrs-swagger-repo/lambda_packages:/var/task/lambdalayer amazonlinux:latest bash