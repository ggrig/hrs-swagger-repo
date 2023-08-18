# HRS Project Green 

## ODS Client

The ODS Client supports ODS endpoints as per [the swagger specification](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/HPP-V2/1.0.0.0)

## OIP Clinet

The OIP Client supports OIP endpoints as per [the swagger specification](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/OIP-API/1.0.0)

## Lambdas

- `run_ods_test.py` sends test requests to the ODS mock [endpoints](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/HPP-V2/1.0.0.0)
- `run_oip_test.py` sends test requests to the OIP mock [endpoints](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/OIP-API/1.0.0)
  
## Lambda Layers

Building the layer for the Lambda fucntions

``
cp -r ods_client python/
cp -r oip_client python/
cd python
pip3 install --target=. -r ../requirements.txt --no-user --no-cache --upgrade
cd ..
zip -r lambda_layer.zip python
``
