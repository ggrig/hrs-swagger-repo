import json
import oip_client

def run(event, context):

    configuration = oip_client.Configuration()
    configuration.access_token = 'YOUR_ACCESS_TOKEN'

    api_instance = oip_client.DefaultApi()
    body = oip_client.AccountingDocument() # AccountingDocument | 

    try:
        # InsertPayment
        api_response = api_instance.accountingdocuments_document_id_put(body, None)
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'accountingdocuments_document_id_put'
        }

    # create an instance of the API class
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
    body = oip_client.BankaccountinfoBody() # BankaccountinfoBody | 

    try:
        # Create Bank Accout Source
        api_response = api_instance.bank_account_info_post(body)
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'bank_account_info_post'
        }

    # create an instance of the API class
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
    body = oip_client.BookingsourceBody() # BookingsourceBody | 

    try:
        # Create Booking Source
        api_response = api_instance.booking_source_post(body)
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'booking_source_post'
        }

    # create an instance of the API class
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
    body = oip_client.CountriesBody() # CountriesBody | 

    try:
        # Create Countries Source
        api_response = api_instance.countries_post(body)
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'countries_post'
        }

    # create an instance of the API class
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
    body = oip_client.HotelsBody() # HotelsBody | 

    try:
        # Create Hotels Source
        api_response = api_instance.hotels_post(body)
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'hotels_post'
        }

    # create an instance of the API class
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
    body = oip_client.PaymentmethodsBody() # PaymentmethodsBody | 

    try:
        # Create Payment Methods Source
        api_response = api_instance.payment_methods_post(body)
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'payment_methods_post'
        }

    # create an instance of the API class
    api_instance = oip_client.DefaultApi(oip_client.ApiClient(configuration))
    body = oip_client.SalespersonBody() # SalespersonBody |

    try:
        # Create Salesperson Source
        api_response = api_instance.salesperson_post(body)
    except ApiException as e:
        return {
            'statusCode': 500,
            'error': str(e),
            'api': 'salesperson_post'
        }

    return {
        'statusCode': 200,
        'error': 'OK'
    }