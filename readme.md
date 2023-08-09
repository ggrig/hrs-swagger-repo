# HRS Project Green 

## ODS Client

The ODS Client supports ODS endpoints as per [the swagger specification](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/HPP/1.0.0.0)

## OIP Clinet

The OIP Client supports OIP endpoints as per [the swagger specification](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/OIP-API/1.0.0)

## Lambdas

- `run_ods_test.py` sends test requests to the ODS mock [endpoints](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/HPP/1.0.0.0)
- `run_oip_test.py` sends test requests to the OIP mock [endpoints](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/OIP-API/1.0.0)
  
## Lambda Layers

Building the layer for the Lambda fucntions

``
cp ods_client pyton/
cp oip_client pyton/
cd python
pip3 install --target=. -r ../requirements.txt --no-user
cd ..
zip -r lambda_layer.zip python
``
