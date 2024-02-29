# winthrop_client_python.ReportingApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coach_contract_requests**](ReportingApi.md#get_coach_contract_requests) | **GET** /api/v1/reports/coach_contract_requests | 
[**get_coach_history**](ReportingApi.md#get_coach_history) | **GET** /api/v1/reports/coach_history | 
[**get_conferenceships**](ReportingApi.md#get_conferenceships) | **GET** /api/v1/reports/conferenceships | 
[**get_foia_details**](ReportingApi.md#get_foia_details) | **GET** /api/v1/reports/foia_details | 
[**get_games**](ReportingApi.md#get_games) | **GET** /api/v1/reports/games | 
[**get_invoices**](ReportingApi.md#get_invoices) | **GET** /api/v1/reports/invoices | 
[**get_school_contract_requests**](ReportingApi.md#get_school_contract_requests) | **GET** /api/v1/reports/school_contract_requests | 
[**get_schools_financials_qc**](ReportingApi.md#get_schools_financials_qc) | **GET** /api/v1/financials_qc | 
[**get_subscriptions**](ReportingApi.md#get_subscriptions) | **GET** /api/v1/reports/subscriptions | 


# **get_coach_contract_requests**
> object get_coach_contract_requests(page=page, q=q)



Retrieve some or all coach contract requests

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_coach_contract_requests(page=page, q=q)
        print("The response of ReportingApi->get_coach_contract_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_coach_contract_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coach contract requests were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coach_history**
> object get_coach_history(page=page, q=q)



Retrieve some or all coach history

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_coach_history(page=page, q=q)
        print("The response of ReportingApi->get_coach_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_coach_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coach history was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conferenceships**
> object get_conferenceships(page=page, q=q)



Retrieve some or all conferenceships

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_conferenceships(page=page, q=q)
        print("The response of ReportingApi->get_conferenceships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_conferenceships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conferenceships were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_details**
> object get_foia_details(page=page, q=q)



Retrieve some or all foia details

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_foia_details(page=page, q=q)
        print("The response of ReportingApi->get_foia_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_foia_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia details were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_games**
> object get_games(page=page, q=q)



Retrieve some or all games

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_games(page=page, q=q)
        print("The response of ReportingApi->get_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_games: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Games were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> object get_invoices(page=page, q=q)



Retrieve some or all client invoices

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_invoices(page=page, q=q)
        print("The response of ReportingApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoices were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_contract_requests**
> object get_school_contract_requests(page=page, q=q)



Retrieve some or all school contract requests

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_school_contract_requests(page=page, q=q)
        print("The response of ReportingApi->get_school_contract_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_school_contract_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | School contract requests were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schools_financials_qc**
> FinancialQc get_schools_financials_qc(page=page, q=q)



Retrieve schools with thier financials qc

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.financial_qc import FinancialQc
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_schools_financials_qc(page=page, q=q)
        print("The response of ReportingApi->get_schools_financials_qc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_schools_financials_qc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**FinancialQc**](FinancialQc.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | some schools with thier financials qc report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> object get_subscriptions(page=page, q=q)



Retrieve subscriptions

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api-gateway.default.svc.cluster.local
# See configuration.py for a list of all supported configuration parameters.
configuration = winthrop_client_python.Configuration(
    host = "http://api-gateway.default.svc.cluster.local"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_subscriptions(page=page, q=q)
        print("The response of ReportingApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | some subscriptions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

