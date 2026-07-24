# winthrop_client_python.CtbApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ctb_compensation_processing_event**](CtbApi.md#create_ctb_compensation_processing_event) | **POST** /api/v1/ctb_compensation_processing_events | 


# **create_ctb_compensation_processing_event**
> CtbCompensationProcessingEventResponse create_ctb_compensation_processing_event(ctb_compensation_processing_event_request)

Atomically apply one reviewed CTB compensation availability exception

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.ctb_compensation_processing_event_request import CtbCompensationProcessingEventRequest
from winthrop_client_python.models.ctb_compensation_processing_event_response import CtbCompensationProcessingEventResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.CtbApi(api_client)
    ctb_compensation_processing_event_request = winthrop_client_python.CtbCompensationProcessingEventRequest() # CtbCompensationProcessingEventRequest | 

    try:
        api_response = api_instance.create_ctb_compensation_processing_event(ctb_compensation_processing_event_request)
        print("The response of CtbApi->create_ctb_compensation_processing_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CtbApi->create_ctb_compensation_processing_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctb_compensation_processing_event_request** | [**CtbCompensationProcessingEventRequest**](CtbCompensationProcessingEventRequest.md)|  | 

### Return type

[**CtbCompensationProcessingEventResponse**](CtbCompensationProcessingEventResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An identical prior CTB decision was returned idempotently |  -  |
**201** | The reviewed CTB compensation decision was applied |  -  |
**409** | Reviewed state changed or the idempotency identity conflicts |  -  |
**422** | Invalid or inconsistent CTB compensation effect |  -  |
**503** | The configured CTB automation actor is unavailable |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

