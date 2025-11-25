# winthrop_client_python.MlAthleticApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check**](MlAthleticApi.md#health_check) | **GET** /ml-athletic/health_check | 
[**predict**](MlAthleticApi.md#predict) | **POST** /ml-athletic/predict | 


# **health_check**
> HealthCheckSuccess health_check()

Check if the model is loaded and the API is running.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.health_check_success import HealthCheckSuccess
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
    api_instance = winthrop_client_python.MlAthleticApi(api_client)

    try:
        api_response = api_instance.health_check()
        print("The response of MlAthleticApi->health_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlAthleticApi->health_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HealthCheckSuccess**](HealthCheckSuccess.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Model is loaded |  -  |
**503** | Failed to load model |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict**
> PredictSuccess predict(predict_body=predict_body)

Classify a job post as athletic or not.

### Example

* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.predict_body import PredictBody
from winthrop_client_python.models.predict_success import PredictSuccess
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.MlAthleticApi(api_client)
    predict_body = winthrop_client_python.PredictBody() # PredictBody |  (optional)

    try:
        api_response = api_instance.predict(predict_body=predict_body)
        print("The response of MlAthleticApi->predict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MlAthleticApi->predict: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predict_body** | [**PredictBody**](PredictBody.md)|  | [optional] 

### Return type

[**PredictSuccess**](PredictSuccess.md)

### Authorization

[Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job Post classified |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

