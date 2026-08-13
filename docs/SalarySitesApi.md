# winthrop_client_python.SalarySitesApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_salary_site_associations**](SalarySitesApi.md#get_salary_site_associations) | **GET** /api/v1/salary_site_associations | 


# **get_salary_site_associations**
> SalarySiteAssociationsResponse get_salary_site_associations(school_ids, page=page, per_page=per_page)

Retrieve every School↔Site association scoped to salary sites, for a given set of school IDs

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.salary_site_associations_response import SalarySiteAssociationsResponse
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
    api_instance = winthrop_client_python.SalarySitesApi(api_client)
    school_ids = [56] # List[int] | 1 to 100 unique positive school IDs
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int |  (optional) (default to 100)

    try:
        api_response = api_instance.get_salary_site_associations(school_ids, page=page, per_page=per_page)
        print("The response of SalarySitesApi->get_salary_site_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalarySitesApi->get_salary_site_associations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_ids** | [**List[int]**](int.md)| 1 to 100 unique positive school IDs | 
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**|  | [optional] [default to 100]

### Return type

[**SalarySiteAssociationsResponse**](SalarySiteAssociationsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Salary site associations |  -  |
**400** | Invalid or missing school_ids filter, or invalid pagination parameter |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

