
```
docker run --name lambdalayer --rm --env HTTP_PROXY --env HTTPS_PROXY --env NO_PROXY --mount type=bind,source="$(pwd)"/lambda_packages,target=/var/task/lambdalayer -it aws-python3.9:local bash
```