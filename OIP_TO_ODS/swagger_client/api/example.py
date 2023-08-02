from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ModifyInvoiceV4Body() # ModifyInvoiceV4Body | 

try:
    # ModifyInvoiceV4
    api_response = api_instance.modify_invoice_v4(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->modify_invoice_v4: %s\n" % e)
