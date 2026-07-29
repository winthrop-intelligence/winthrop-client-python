# winthrop_client_python.FoiaInboxApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_foia_inbox**](FoiaInboxApi.md#apply_foia_inbox) | **POST** /api/v1/foia_inbox_apply | 
[**get_foia_inbox_candidates**](FoiaInboxApi.md#get_foia_inbox_candidates) | **GET** /api/v1/foia_inbox_candidates | 


# **apply_foia_inbox**
> FoiaInboxApplyResponse apply_foia_inbox(foia_inbox_apply_request)

Atomically apply one approved Gmail message decision to one FOIA request. A retry whose selected final state is already present returns already_applied without duplicating effects.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_inbox_apply_request import FoiaInboxApplyRequest
from winthrop_client_python.models.foia_inbox_apply_response import FoiaInboxApplyResponse
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
    api_instance = winthrop_client_python.FoiaInboxApi(api_client)
    foia_inbox_apply_request = winthrop_client_python.FoiaInboxApplyRequest() # FoiaInboxApplyRequest | 

    try:
        api_response = api_instance.apply_foia_inbox(foia_inbox_apply_request)
        print("The response of FoiaInboxApi->apply_foia_inbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoiaInboxApi->apply_foia_inbox: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_inbox_apply_request** | [**FoiaInboxApplyRequest**](FoiaInboxApplyRequest.md)|  | 

### Return type

[**FoiaInboxApplyResponse**](FoiaInboxApplyResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The approved decision was applied, or its selected final state was already present |  -  |
**409** | Reviewed state changed and the selected final state is not already present |  -  |
**422** | Invalid or inconsistent effect bundle |  -  |
**503** | The configured FOIA inbox automation actor is unavailable |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_inbox_candidates**
> FoiaInboxCandidatesResponse get_foia_inbox_candidates(page=page, per_page=per_page, school_id=school_id, foia_request_id=foia_request_id, if_none_match=if_none_match)

Retrieve active FOIA requests on active labels for explainable inbox matching

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_inbox_candidates_response import FoiaInboxCandidatesResponse
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
    api_instance = winthrop_client_python.FoiaInboxApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)
    school_id = 56 # int |  (optional)
    foia_request_id = 56 # int |  (optional)
    if_none_match = 'if_none_match_example' # str | ETag from a previous response; when it still matches, the server responds 304 Not Modified instead of re-sending the payload. (optional)

    try:
        api_response = api_instance.get_foia_inbox_candidates(page=page, per_page=per_page, school_id=school_id, foia_request_id=foia_request_id, if_none_match=if_none_match)
        print("The response of FoiaInboxApi->get_foia_inbox_candidates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoiaInboxApi->get_foia_inbox_candidates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]
 **school_id** | **int**|  | [optional] 
 **foia_request_id** | **int**|  | [optional] 
 **if_none_match** | **str**| ETag from a previous response; when it still matches, the server responds 304 Not Modified instead of re-sending the payload. | [optional] 

### Return type

[**FoiaInboxCandidatesResponse**](FoiaInboxCandidatesResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active FOIA inbox matching candidates |  * ETag - Entity tag for the current review context; send it back via If-None-Match for conditional requests. <br>  |
**304** | Not Modified — the candidate page matching the ETag supplied in If-None-Match is still current; no body is returned. |  -  |
**400** | Invalid filter or pagination parameter |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

