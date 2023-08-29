# HRS Project Green 

## ODS Client

The ODS Client supports ODS endpoints as per [the swagger specification](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/HPP-V2/1.0.0.0)

## OIP Clinet

The OIP Client supports OIP endpoints as per [the swagger specification](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/OIP-API/1.0.0)

## Lambdas

- `run_ods_test.py` sends test requests to the ODS mock [endpoints](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/HPP-V2/1.0.0.0)
- `run_oip_test.py` sends test requests to the OIP mock [endpoints](https://app.swaggerhub.com/apis-docs/Marquardt-Informatik/OIP-API/1.0.0)
  
## Building the Lambda fucntions Layer

### Windows PowerShell

``
python -m venv lambda_layer  
cp -r python lambda_layer/  
cp -r ods_client lambda_layer/python/  
cp -r oip_client lambda_layer/python/  
cd lambda_layer/  
Scripts\activate  
cd python/  
python.exe -m pip install --upgrade pip  
pip3 install --target=. -r requirements.txt --no-user --no-cache  
cd ..  
deactivate  
``
Then ZIP the `lambda_layer/python/` folder to python.zip

### AWS Linux Terminal

``
python3 -m venv lambda_layer  
cp -r python lambda_layer/  
cp -r ods_client lambda_layer/python/  
cp -r oip_client lambda_layer/python/  
cd lambda_layer/  
source bin/activate  
cd python  
python3 -m pip install --upgrade pip  
pip3 install --target=. -r requirements.txt --no-user --no-cache  
cd ..  
deactivate  
zip -r lambda_layer.zip python  
``
