import json
import oip_client

def run(event, context):

    configuration = oip_client.Configuration()
    configuration.access_token = 'YOUR_ACCESS_TOKEN'

    # create an instance of the API class
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
    body = oip_client.SalespersonBody() # SalespersonBody |

    try:
        # Create Booking Source
        api_response = api_instance.salesperson_post(body)
        return {
            'statusCode': 200,
            'error': 'OK'
        }
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }
