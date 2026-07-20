# winthrop_client_python.OcrApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_ocr_v1_jobs_post**](OcrApi.md#create_job_ocr_v1_jobs_post) | **POST** /ocr/v1/jobs | Submit an OCR job for a Google Drive file
[**job_result_ocr_v1_jobs_job_id_result_get**](OcrApi.md#job_result_ocr_v1_jobs_job_id_result_get) | **GET** /ocr/v1/jobs/{job_id}/result | Fetch the full result
[**job_status_batch_ocr_v1_jobs_get**](OcrApi.md#job_status_batch_ocr_v1_jobs_get) | **GET** /ocr/v1/jobs | Poll many jobs in one request
[**job_status_ocr_v1_jobs_job_id_get**](OcrApi.md#job_status_ocr_v1_jobs_job_id_get) | **GET** /ocr/v1/jobs/{job_id} | Poll one job


# **create_job_ocr_v1_jobs_post**
> JobAccepted create_job_ocr_v1_jobs_post(create_job_json)

Submit an OCR job for a Google Drive file

The service downloads the file with its service account and OCRs every page through Mistral. Returns 202 with a job id to poll. Resubmitting an identical file (same client, same resolved policy) resolves to the prior result during preparation instead of re-paying for OCR; pass options.force to reprocess.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.create_job_json import CreateJobJson
from winthrop_client_python.models.job_accepted import JobAccepted
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
    api_instance = winthrop_client_python.OcrApi(api_client)
    create_job_json = winthrop_client_python.CreateJobJson() # CreateJobJson | 

    try:
        # Submit an OCR job for a Google Drive file
        api_response = api_instance.create_job_ocr_v1_jobs_post(create_job_json)
        print("The response of OcrApi->create_job_ocr_v1_jobs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrApi->create_job_ocr_v1_jobs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_job_json** | [**CreateJobJson**](CreateJobJson.md)|  | 

### Return type

[**JobAccepted**](JobAccepted.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful Response |  -  |
**422** | Invalid profile or options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_result_ocr_v1_jobs_job_id_result_get**
> JobResult job_result_ocr_v1_jobs_job_id_result_get(job_id)

Fetch the full result

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job_result import JobResult
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
    api_instance = winthrop_client_python.OcrApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Fetch the full result
        api_response = api_instance.job_result_ocr_v1_jobs_job_id_result_get(job_id)
        print("The response of OcrApi->job_result_ocr_v1_jobs_job_id_result_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrApi->job_result_ocr_v1_jobs_job_id_result_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**JobResult**](JobResult.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_status_batch_ocr_v1_jobs_get**
> JobStatusBatch job_status_batch_ocr_v1_jobs_get(ids)

Poll many jobs in one request

Comma-separated `ids` (e.g. `?ids=a,b,c`). Returns the status of the caller's own jobs among them; unknown, expired, or other clients' ids come back in `not_found`. At most 100 ids per call.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job_status_batch import JobStatusBatch
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
    api_instance = winthrop_client_python.OcrApi(api_client)
    ids = 'ids_example' # str | 

    try:
        # Poll many jobs in one request
        api_response = api_instance.job_status_batch_ocr_v1_jobs_get(ids)
        print("The response of OcrApi->job_status_batch_ocr_v1_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrApi->job_status_batch_ocr_v1_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**|  | 

### Return type

[**JobStatusBatch**](JobStatusBatch.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Missing or too many ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_status_ocr_v1_jobs_job_id_get**
> JobStatus job_status_ocr_v1_jobs_job_id_get(job_id)

Poll one job

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job_status import JobStatus
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
    api_instance = winthrop_client_python.OcrApi(api_client)
    job_id = 'job_id_example' # str | 

    try:
        # Poll one job
        api_response = api_instance.job_status_ocr_v1_jobs_job_id_get(job_id)
        print("The response of OcrApi->job_status_ocr_v1_jobs_job_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OcrApi->job_status_ocr_v1_jobs_job_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**|  | 

### Return type

[**JobStatus**](JobStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

