# winthrop_client_python.DossierApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**university_dossier_report_dossier_winad_id_get**](DossierApi.md#university_dossier_report_dossier_winad_id_get) | **GET** /api/v1/dossier/{winad_id}/ | University Dossier Report


# **university_dossier_report_dossier_winad_id_get**
> DossierReportResponse university_dossier_report_dossier_winad_id_get(winad_id)

University Dossier Report

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.dossier_report_response import DossierReportResponse
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
    api_instance = winthrop_client_python.DossierApi(api_client)
    winad_id = 56 # int | 

    try:
        # University Dossier Report
        api_response = api_instance.university_dossier_report_dossier_winad_id_get(winad_id)
        print("The response of DossierApi->university_dossier_report_dossier_winad_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DossierApi->university_dossier_report_dossier_winad_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **winad_id** | **int**|  | 

### Return type

[**DossierReportResponse**](DossierReportResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

