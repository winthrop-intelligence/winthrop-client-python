# winthrop_client_python.ReportingApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_reports_coach_contract_requests_get**](ReportingApi.md#api_v1_reports_coach_contract_requests_get) | **GET** /api/v1/reports/coach_contract_requests | 
[**api_v1_reports_coach_history_get**](ReportingApi.md#api_v1_reports_coach_history_get) | **GET** /api/v1/reports/coach_history | 
[**api_v1_reports_conferenceships_get**](ReportingApi.md#api_v1_reports_conferenceships_get) | **GET** /api/v1/reports/conferenceships | 
[**api_v1_reports_foia_details_get**](ReportingApi.md#api_v1_reports_foia_details_get) | **GET** /api/v1/reports/foia_details | 
[**api_v1_reports_games_get**](ReportingApi.md#api_v1_reports_games_get) | **GET** /api/v1/reports/games | 
[**api_v1_reports_invoices_get**](ReportingApi.md#api_v1_reports_invoices_get) | **GET** /api/v1/reports/invoices | 
[**api_v1_reports_school_contract_requests_get**](ReportingApi.md#api_v1_reports_school_contract_requests_get) | **GET** /api/v1/reports/school_contract_requests | 
[**api_v1_reports_subscriptions_get**](ReportingApi.md#api_v1_reports_subscriptions_get) | **GET** /api/v1/reports/subscriptions | 


# **api_v1_reports_coach_contract_requests_get**
> api_v1_reports_coach_contract_requests_get(page=page, q=q)



Retrieve some or all coach contract requests

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_coach_contract_requests_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_coach_contract_requests_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

# **api_v1_reports_coach_history_get**
> api_v1_reports_coach_history_get(page=page, q=q)



Retrieve some or all coach history

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_coach_history_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_coach_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

# **api_v1_reports_conferenceships_get**
> api_v1_reports_conferenceships_get(page=page, q=q)



Retrieve some or all conferenceships

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_conferenceships_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_conferenceships_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

# **api_v1_reports_foia_details_get**
> api_v1_reports_foia_details_get(page=page, q=q)



Retrieve some or all foia details

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_foia_details_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_foia_details_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

# **api_v1_reports_games_get**
> api_v1_reports_games_get(page=page, q=q)



Retrieve some or all games

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_games_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_games_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

# **api_v1_reports_invoices_get**
> api_v1_reports_invoices_get(page=page, q=q)



Retrieve some or all client invoices

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_invoices_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_invoices_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

# **api_v1_reports_school_contract_requests_get**
> api_v1_reports_school_contract_requests_get(page=page, q=q)



Retrieve some or all school contract requests

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_school_contract_requests_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_school_contract_requests_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

# **api_v1_reports_subscriptions_get**
> api_v1_reports_subscriptions_get(page=page, q=q)



Retrieve subscriptions

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
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
        api_instance.api_v1_reports_subscriptions_get(page=page, q=q)
    except Exception as e:
        print("Exception when calling ReportingApi->api_v1_reports_subscriptions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

void (empty response body)

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

