# swagger_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/Marquardt-Informatik/OIP-API/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountingdocuments_document_id_put**](DefaultApi.md#accountingdocuments_document_id_put) | **PUT** /accountingdocuments/{documentId} | Update Accounting Document
[**bank_account_info_post**](DefaultApi.md#bank_account_info_post) | **POST** /bank-account-info | Submit Bank Account Information
[**booking_source_post**](DefaultApi.md#booking_source_post) | **POST** /booking-source | Create Booking Source
[**countries_post**](DefaultApi.md#countries_post) | **POST** /countries | Create Country
[**hotels_post**](DefaultApi.md#hotels_post) | **POST** /hotels | Create Hotel
[**payment_methods_post**](DefaultApi.md#payment_methods_post) | **POST** /payment-methods | Create Payment Method
[**salesperson_post**](DefaultApi.md#salesperson_post) | **POST** /salesperson | Create Salesperson

# **accountingdocuments_document_id_put**
> accountingdocuments_document_id_put(body, document_id)

Update Accounting Document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.AccountingDocument() # AccountingDocument | 
document_id = 'document_id_example' # str | ID of the Accounting Document to update

try:
    # Update Accounting Document
    api_instance.accountingdocuments_document_id_put(body, document_id)
except ApiException as e:
    print("Exception when calling DefaultApi->accountingdocuments_document_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountingDocument**](AccountingDocument.md)|  | 
 **document_id** | **str**| ID of the Accounting Document to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_account_info_post**
> InlineResponse200 bank_account_info_post(body)

Submit Bank Account Information

Submits bank account information to the Online Invoice Portal (OIP).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.BankaccountinfoBody() # BankaccountinfoBody | 

try:
    # Submit Bank Account Information
    api_response = api_instance.bank_account_info_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->bank_account_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BankaccountinfoBody**](BankaccountinfoBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **booking_source_post**
> InlineResponse2001 booking_source_post(body)

Create Booking Source

Creates a new booking source.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.BookingsourceBody() # BookingsourceBody | 

try:
    # Create Booking Source
    api_response = api_instance.booking_source_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->booking_source_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BookingsourceBody**](BookingsourceBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countries_post**
> InlineResponse2001 countries_post(body)

Create Country

Creates a new country entry.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.CountriesBody() # CountriesBody | 

try:
    # Create Country
    api_response = api_instance.countries_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->countries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CountriesBody**](CountriesBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hotels_post**
> InlineResponse2001 hotels_post(body)

Create Hotel

Creates a new hotel entry.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.HotelsBody() # HotelsBody | 

try:
    # Create Hotel
    api_response = api_instance.hotels_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hotels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HotelsBody**](HotelsBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_methods_post**
> InlineResponse2001 payment_methods_post(body)

Create Payment Method

Creates a new payment method entry.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.PaymentmethodsBody() # PaymentmethodsBody | 

try:
    # Create Payment Method
    api_response = api_instance.payment_methods_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->payment_methods_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentmethodsBody**](PaymentmethodsBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salesperson_post**
> InlineResponse2001 salesperson_post(body)

Create Salesperson

Creates a new salesperson entry.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.SalespersonBody() # SalespersonBody | 

try:
    # Create Salesperson
    api_response = api_instance.salesperson_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->salesperson_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SalespersonBody**](SalespersonBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

