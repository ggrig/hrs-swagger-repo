# swagger_client.HPPBindingApi

All URIs are relative to *https://virtserver.swaggerhub.com/Marquardt-Informatik/HPP-V2/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_contact_information**](HPPBindingApi.md#change_contact_information) | **POST** /ChangeContactInformation | ChangeContactInformation
[**change_customer_address**](HPPBindingApi.md#change_customer_address) | **POST** /ChangeCustomerAddress | ChangeCustomerAddress
[**change_customer_address_v2**](HPPBindingApi.md#change_customer_address_v2) | **POST** /ChangeCustomerAddressV2 | ChangeCustomerAddressV2
[**change_invoice_address**](HPPBindingApi.md#change_invoice_address) | **POST** /ChangeInvoiceAddress | ChangeInvoiceAddress
[**confirm_invoice**](HPPBindingApi.md#confirm_invoice) | **POST** /ConfirmInvoice | ConfirmInvoice
[**insert_payment**](HPPBindingApi.md#insert_payment) | **POST** /InsertPayment | InsertPayment
[**insert_payment_pc**](HPPBindingApi.md#insert_payment_pc) | **POST** /InsertPaymentPC | InsertPaymentPC
[**insert_payment_v2**](HPPBindingApi.md#insert_payment_v2) | **POST** /InsertPaymentV2 | InsertPaymentV2
[**insert_payment_v3**](HPPBindingApi.md#insert_payment_v3) | **POST** /InsertPaymentV3 | InsertPaymentV3
[**modify_hotel_bank_account_info**](HPPBindingApi.md#modify_hotel_bank_account_info) | **POST** /ModifyHotelBankAccountInfo | ModifyHotelBankAccountInfo
[**modify_hotel_credit_card_info**](HPPBindingApi.md#modify_hotel_credit_card_info) | **POST** /ModifyHotelCreditCardInfo | ModifyHotelCreditCardInfo
[**modify_invoice**](HPPBindingApi.md#modify_invoice) | **POST** /ModifyInvoice | ModifyInvoice
[**modify_invoice_v2**](HPPBindingApi.md#modify_invoice_v2) | **POST** /ModifyInvoiceV2 | ModifyInvoiceV2
[**modify_invoice_v3**](HPPBindingApi.md#modify_invoice_v3) | **POST** /ModifyInvoiceV3 | ModifyInvoiceV3
[**modify_invoice_v4**](HPPBindingApi.md#modify_invoice_v4) | **POST** /ModifyInvoiceV4 | ModifyInvoiceV4

# **change_contact_information**
> InlineResponse2002 change_contact_information(body)

ChangeContactInformation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ChangeContactInformationBody() # ChangeContactInformationBody | 

try:
    # ChangeContactInformation
    api_response = api_instance.change_contact_information(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->change_contact_information: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeContactInformationBody**](ChangeContactInformationBody.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_customer_address**
> InlineResponse2001 change_customer_address(body)

ChangeCustomerAddress

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ChangeCustomerAddressBody() # ChangeCustomerAddressBody | 

try:
    # ChangeCustomerAddress
    api_response = api_instance.change_customer_address(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->change_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeCustomerAddressBody**](ChangeCustomerAddressBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_customer_address_v2**
> InlineResponse2006 change_customer_address_v2(body)

ChangeCustomerAddressV2

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ChangeCustomerAddressV2Body() # ChangeCustomerAddressV2Body | 

try:
    # ChangeCustomerAddressV2
    api_response = api_instance.change_customer_address_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->change_customer_address_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeCustomerAddressV2Body**](ChangeCustomerAddressV2Body.md)|  | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_invoice_address**
> InlineResponse200 change_invoice_address(body)

ChangeInvoiceAddress

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ChangeInvoiceAddressBody() # ChangeInvoiceAddressBody | 

try:
    # ChangeInvoiceAddress
    api_response = api_instance.change_invoice_address(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->change_invoice_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeInvoiceAddressBody**](ChangeInvoiceAddressBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_invoice**
> InlineResponse20011 confirm_invoice(body)

ConfirmInvoice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ConfirmInvoiceBody() # ConfirmInvoiceBody | 

try:
    # ConfirmInvoice
    api_response = api_instance.confirm_invoice(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->confirm_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfirmInvoiceBody**](ConfirmInvoiceBody.md)|  | 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_payment**
> InlineResponse2003 insert_payment(body)

InsertPayment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.InsertPaymentBody() # InsertPaymentBody | 

try:
    # InsertPayment
    api_response = api_instance.insert_payment(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->insert_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertPaymentBody**](InsertPaymentBody.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_payment_pc**
> InlineResponse20014 insert_payment_pc(body)

InsertPaymentPC

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.InsertPaymentPCBody() # InsertPaymentPCBody | 

try:
    # InsertPaymentPC
    api_response = api_instance.insert_payment_pc(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->insert_payment_pc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertPaymentPCBody**](InsertPaymentPCBody.md)|  | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_payment_v2**
> InlineResponse2005 insert_payment_v2(body)

InsertPaymentV2

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.InsertPaymentV2Body() # InsertPaymentV2Body | 

try:
    # InsertPaymentV2
    api_response = api_instance.insert_payment_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->insert_payment_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertPaymentV2Body**](InsertPaymentV2Body.md)|  | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_payment_v3**
> InlineResponse2009 insert_payment_v3(body)

InsertPaymentV3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.InsertPaymentV3Body() # InsertPaymentV3Body | 

try:
    # InsertPaymentV3
    api_response = api_instance.insert_payment_v3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->insert_payment_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InsertPaymentV3Body**](InsertPaymentV3Body.md)|  | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_hotel_bank_account_info**
> InlineResponse20013 modify_hotel_bank_account_info(body)

ModifyHotelBankAccountInfo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ModifyHotelBankAccountInfoBody() # ModifyHotelBankAccountInfoBody | 

try:
    # ModifyHotelBankAccountInfo
    api_response = api_instance.modify_hotel_bank_account_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->modify_hotel_bank_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyHotelBankAccountInfoBody**](ModifyHotelBankAccountInfoBody.md)|  | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_hotel_credit_card_info**
> InlineResponse20012 modify_hotel_credit_card_info(body)

ModifyHotelCreditCardInfo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ModifyHotelCreditCardInfoBody() # ModifyHotelCreditCardInfoBody | 

try:
    # ModifyHotelCreditCardInfo
    api_response = api_instance.modify_hotel_credit_card_info(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->modify_hotel_credit_card_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyHotelCreditCardInfoBody**](ModifyHotelCreditCardInfoBody.md)|  | 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_invoice**
> InlineResponse2004 modify_invoice(body)

ModifyInvoice

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ModifyInvoiceBody() # ModifyInvoiceBody | 

try:
    # ModifyInvoice
    api_response = api_instance.modify_invoice(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->modify_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyInvoiceBody**](ModifyInvoiceBody.md)|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_invoice_v2**
> InlineResponse2007 modify_invoice_v2(body)

ModifyInvoiceV2

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ModifyInvoiceV2Body() # ModifyInvoiceV2Body | 

try:
    # ModifyInvoiceV2
    api_response = api_instance.modify_invoice_v2(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->modify_invoice_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyInvoiceV2Body**](ModifyInvoiceV2Body.md)|  | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_invoice_v3**
> InlineResponse2008 modify_invoice_v3(body)

ModifyInvoiceV3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HPPBindingApi()
body = swagger_client.ModifyInvoiceV3Body() # ModifyInvoiceV3Body | 

try:
    # ModifyInvoiceV3
    api_response = api_instance.modify_invoice_v3(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HPPBindingApi->modify_invoice_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyInvoiceV3Body**](ModifyInvoiceV3Body.md)|  | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_invoice_v4**
> InlineResponse20010 modify_invoice_v4(body)

ModifyInvoiceV4

### Example
```python
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModifyInvoiceV4Body**](ModifyInvoiceV4Body.md)|  | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

