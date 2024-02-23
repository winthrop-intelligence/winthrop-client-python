# winthrop_client_python.DefaultApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_foia_label**](DefaultApi.md#create_foia_label) | **POST** /api/v1/foia_labels | 
[**create_foia_request**](DefaultApi.md#create_foia_request) | **POST** /api/v1/foia_requests | 
[**create_job_post**](DefaultApi.md#create_job_post) | **POST** /central_jobs/job_posts | Create a job post
[**create_requested_item**](DefaultApi.md#create_requested_item) | **POST** /api/v1/requested_items | 
[**delete_foia_label**](DefaultApi.md#delete_foia_label) | **DELETE** /api/v1/foia_labels/{foiaLabelId} | 
[**delete_foia_request**](DefaultApi.md#delete_foia_request) | **DELETE** /api/v1/foia_requests/{foiaRequestId} | 
[**delete_job_post**](DefaultApi.md#delete_job_post) | **DELETE** /central_jobs/job_posts/{jobPostId} | Delete a job post
[**delete_requested_item**](DefaultApi.md#delete_requested_item) | **DELETE** /api/v1/requested_items/{requestedItemId} | 
[**get_administrator**](DefaultApi.md#get_administrator) | **GET** /api/v1/administrators/{administratorId} | 
[**get_administrators**](DefaultApi.md#get_administrators) | **GET** /api/v1/administrators | 
[**get_audited_financial_report_status**](DefaultApi.md#get_audited_financial_report_status) | **GET** /api/v1/audited_financial_report_statuses/{auditedFinancialReportStatusId} | 
[**get_audited_financial_report_statuses**](DefaultApi.md#get_audited_financial_report_statuses) | **GET** /api/v1/audited_financial_report_statuses | 
[**get_categories**](DefaultApi.md#get_categories) | **GET** /central_jobs/categories | List all categories
[**get_coach**](DefaultApi.md#get_coach) | **GET** /api/v1/coaches/{coachId} | 
[**get_coaches**](DefaultApi.md#get_coaches) | **GET** /api/v1/coaches | 
[**get_compensation**](DefaultApi.md#get_compensation) | **GET** /api/v1/compensations/{compensationId} | 
[**get_compensations**](DefaultApi.md#get_compensations) | **GET** /api/v1/compensations | 
[**get_contract**](DefaultApi.md#get_contract) | **GET** /api/v1/contracts/{contractId} | 
[**get_contracts**](DefaultApi.md#get_contracts) | **GET** /api/v1/contracts | 
[**get_deal_status**](DefaultApi.md#get_deal_status) | **GET** /api/v1/deal_statuses/{dealStatusId} | 
[**get_deal_statuses**](DefaultApi.md#get_deal_statuses) | **GET** /api/v1/deal_statuses | 
[**get_foia_label**](DefaultApi.md#get_foia_label) | **GET** /api/v1/foia_labels/{foiaLabelId} | 
[**get_foia_labels**](DefaultApi.md#get_foia_labels) | **GET** /api/v1/foia_labels | 
[**get_foia_request**](DefaultApi.md#get_foia_request) | **GET** /api/v1/foia_requests/{foiaRequestId} | 
[**get_foia_requests**](DefaultApi.md#get_foia_requests) | **GET** /api/v1/foia_requests | 
[**get_game**](DefaultApi.md#get_game) | **GET** /api/v1/games/{gameId} | 
[**get_games**](DefaultApi.md#get_games) | **GET** /api/v1/games | 
[**get_income_report**](DefaultApi.md#get_income_report) | **GET** /api/v1/income_reports/{incomeReportId} | 
[**get_income_reports**](DefaultApi.md#get_income_reports) | **GET** /api/v1/income_reports | 
[**get_job_post**](DefaultApi.md#get_job_post) | **GET** /central_jobs/job_posts/{jobPostId} | Get a job post
[**get_job_posts**](DefaultApi.md#get_job_posts) | **GET** /central_jobs/job_posts | List all job posts
[**get_ncaa_financial_report_status**](DefaultApi.md#get_ncaa_financial_report_status) | **GET** /api/v1/ncaa_financial_report_statuses/{ncaaFinancialReportStatusId} | 
[**get_ncaa_financial_report_statuses**](DefaultApi.md#get_ncaa_financial_report_statuses) | **GET** /api/v1/ncaa_financial_report_statuses | 
[**get_position**](DefaultApi.md#get_position) | **GET** /api/v1/positions/{positionId} | 
[**get_positions**](DefaultApi.md#get_positions) | **GET** /api/v1/positions | 
[**get_requested_item**](DefaultApi.md#get_requested_item) | **GET** /api/v1/requested_items/{requestedItemId} | 
[**get_requested_items**](DefaultApi.md#get_requested_items) | **GET** /api/v1/requested_items | 
[**get_school**](DefaultApi.md#get_school) | **GET** /api/v1/schools/{schoolId} | 
[**get_schools**](DefaultApi.md#get_schools) | **GET** /api/v1/schools | 
[**get_season**](DefaultApi.md#get_season) | **GET** /api/v1/seasons/{seasonId} | 
[**get_seasons**](DefaultApi.md#get_seasons) | **GET** /api/v1/seasons | 
[**get_sport**](DefaultApi.md#get_sport) | **GET** /api/v1/sports/{sportId} | 
[**get_sports**](DefaultApi.md#get_sports) | **GET** /api/v1/sports | 
[**get_user**](DefaultApi.md#get_user) | **GET** /api/v1/users/{userId} | 
[**get_users**](DefaultApi.md#get_users) | **GET** /api/v1/users | 
[**summarizer_post_qa_s3**](DefaultApi.md#summarizer_post_qa_s3) | **POST** /summarizer/qa_s3 | Answer questions over a file from S3
[**summarizer_post_summarize_s3**](DefaultApi.md#summarizer_post_summarize_s3) | **POST** /summarizer/summarize_s3 | Summarize a file from S3
[**update_coach**](DefaultApi.md#update_coach) | **PATCH** /api/v1/coaches/{coachId} | 
[**update_foia_label**](DefaultApi.md#update_foia_label) | **PATCH** /api/v1/foia_labels/{foiaLabelId} | 
[**update_foia_request**](DefaultApi.md#update_foia_request) | **PATCH** /api/v1/foia_requests/{foiaRequestId} | 
[**update_job_post**](DefaultApi.md#update_job_post) | **PATCH** /central_jobs/job_posts/{jobPostId} | Update a job post
[**update_requested_item**](DefaultApi.md#update_requested_item) | **PATCH** /api/v1/requested_items/{requestedItemId} | 


# **create_foia_label**
> FoiaLabel create_foia_label(foia_label)



Create a new foia label

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_label import FoiaLabel
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_label = winthrop_client_python.FoiaLabel() # FoiaLabel | Foia label to create

    try:
        api_response = api_instance.create_foia_label(foia_label)
        print("The response of DefaultApi->create_foia_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_foia_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_label** | [**FoiaLabel**](FoiaLabel.md)| Foia label to create | 

### Return type

[**FoiaLabel**](FoiaLabel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Foia label was created |  -  |
**401** | Unauthorized |  -  |
**422** | Unable to create foia label |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_foia_request**
> FoiaRequest create_foia_request(foia_request)



Create a new foia request

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_request import FoiaRequest
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_request = winthrop_client_python.FoiaRequest() # FoiaRequest | Foia request to create

    try:
        api_response = api_instance.create_foia_request(foia_request)
        print("The response of DefaultApi->create_foia_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_foia_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_request** | [**FoiaRequest**](FoiaRequest.md)| Foia request to create | 

### Return type

[**FoiaRequest**](FoiaRequest.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Foia request was created |  -  |
**401** | Unauthorized |  -  |
**422** | Unable to create foia request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_post**
> JobPost create_job_post(job_post=job_post)

Create a job post

Create a job post

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.job_post import JobPost
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    job_post = winthrop_client_python.JobPost() # JobPost |  (optional)

    try:
        # Create a job post
        api_response = api_instance.create_job_post(job_post=job_post)
        print("The response of DefaultApi->create_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_post** | [**JobPost**](JobPost.md)|  | [optional] 

### Return type

[**JobPost**](JobPost.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job post was created |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_requested_item**
> RequestedItem create_requested_item(requested_item)



Create a new requested item

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.requested_item import RequestedItem
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    requested_item = winthrop_client_python.RequestedItem() # RequestedItem | Requested item to create

    try:
        api_response = api_instance.create_requested_item(requested_item)
        print("The response of DefaultApi->create_requested_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_requested_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_item** | [**RequestedItem**](RequestedItem.md)| Requested item to create | 

### Return type

[**RequestedItem**](RequestedItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Requested item was created |  -  |
**401** | Unauthorized |  -  |
**422** | Unable to create requested item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_foia_label**
> delete_foia_label(foia_label_id)



Delete a single foia label

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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_label_id = 56 # int | ID of foia label to delete

    try:
        api_instance.delete_foia_label(foia_label_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_foia_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_label_id** | **int**| ID of foia label to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Foia label was deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_foia_request**
> delete_foia_request(foia_request_id)



Delete a single foia request

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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_request_id = 56 # int | ID of foia request to delete

    try:
        api_instance.delete_foia_request(foia_request_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_foia_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_request_id** | **int**| ID of foia request to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Foia request was deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_post**
> delete_job_post(job_post_id)

Delete a job post

Delete a job post

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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    job_post_id = 56 # int | ID of job post to delete

    try:
        # Delete a job post
        api_instance.delete_job_post(job_post_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_post_id** | **int**| ID of job post to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Job post was deleted |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_requested_item**
> delete_requested_item(requested_item_id)



Delete a single requested item

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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    requested_item_id = 56 # int | ID of requested item to delete

    try:
        api_instance.delete_requested_item(requested_item_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_requested_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_item_id** | **int**| ID of requested item to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Requested item was deleted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_administrator**
> Administrator get_administrator(administrator_id)



Retrieve a single administrator

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.administrator import Administrator
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    administrator_id = 56 # int | ID of administrator to retrieve

    try:
        api_response = api_instance.get_administrator(administrator_id)
        print("The response of DefaultApi->get_administrator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_administrator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **administrator_id** | **int**| ID of administrator to retrieve | 

### Return type

[**Administrator**](Administrator.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Administrator was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_administrators**
> AdministratorCollection get_administrators(page=page, per_page=per_page, q=q)



Retrieve some or all administrators

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.administrator_collection import AdministratorCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_administrators(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_administrators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_administrators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**AdministratorCollection**](AdministratorCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Administrators were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audited_financial_report_status**
> AuditedFinancialReportStatus get_audited_financial_report_status(audited_financial_report_status_id)



Retrieve a single audited financial report status

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.audited_financial_report_status import AuditedFinancialReportStatus
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    audited_financial_report_status_id = 56 # int | ID of audited financial report status to retrieve

    try:
        api_response = api_instance.get_audited_financial_report_status(audited_financial_report_status_id)
        print("The response of DefaultApi->get_audited_financial_report_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_audited_financial_report_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audited_financial_report_status_id** | **int**| ID of audited financial report status to retrieve | 

### Return type

[**AuditedFinancialReportStatus**](AuditedFinancialReportStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audited financial report status was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audited_financial_report_statuses**
> AuditedFinancialReportStatusCollection get_audited_financial_report_statuses(page=page, per_page=per_page, q=q)



Retrieve some or all audited financial report statuses

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.audited_financial_report_status_collection import AuditedFinancialReportStatusCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_audited_financial_report_statuses(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_audited_financial_report_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_audited_financial_report_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**AuditedFinancialReportStatusCollection**](AuditedFinancialReportStatusCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Audited financial report statuses were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> CategoryCollection get_categories(page=page, per_page=per_page, q=q)

List all categories

List all categories

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.category_collection import CategoryCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        # List all categories
        api_response = api_instance.get_categories(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**CategoryCollection**](CategoryCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Categories were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coach**
> Coach get_coach(coach_id)



Retrieve a single coach

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.coach import Coach
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    coach_id = 56 # int | ID of coach to retrieve

    try:
        api_response = api_instance.get_coach(coach_id)
        print("The response of DefaultApi->get_coach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_coach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coach_id** | **int**| ID of coach to retrieve | 

### Return type

[**Coach**](Coach.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coach was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coaches**
> CoachCollection get_coaches(page=page, per_page=per_page, q=q)



Retrieve some or all coaches

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.coach_collection import CoachCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_coaches(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_coaches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_coaches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**CoachCollection**](CoachCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coaches were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compensation**
> Compensation get_compensation(compensation_id)



Retrieve a single compensation

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.compensation import Compensation
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    compensation_id = 56 # int | ID of compensation to retrieve

    try:
        api_response = api_instance.get_compensation(compensation_id)
        print("The response of DefaultApi->get_compensation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_compensation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compensation_id** | **int**| ID of compensation to retrieve | 

### Return type

[**Compensation**](Compensation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compensation was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compensations**
> CompensationCollection get_compensations(page=page, per_page=per_page, q=q)



Retrieve some or all compensations

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.compensation_collection import CompensationCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_compensations(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_compensations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_compensations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**CompensationCollection**](CompensationCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compensations were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract**
> Contract get_contract(contract_id)



Retrieve a single contract

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.contract import Contract
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    contract_id = 56 # int | ID of contract to retrieve

    try:
        api_response = api_instance.get_contract(contract_id)
        print("The response of DefaultApi->get_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of contract to retrieve | 

### Return type

[**Contract**](Contract.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contracts**
> ContractCollection get_contracts(page=page, per_page=per_page, q=q)



Retrieve some or all contracts

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.contract_collection import ContractCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_contracts(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**ContractCollection**](ContractCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contracts were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_status**
> DealStatus get_deal_status(deal_status_id)



Retrieve a single deal status

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.deal_status import DealStatus
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    deal_status_id = 56 # int | ID of deal status to retrieve

    try:
        api_response = api_instance.get_deal_status(deal_status_id)
        print("The response of DefaultApi->get_deal_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_deal_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deal_status_id** | **int**| ID of deal status to retrieve | 

### Return type

[**DealStatus**](DealStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deal status was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deal_statuses**
> DealStatusCollection get_deal_statuses(page=page, per_page=per_page, q=q)



Retrieve some or all deal statuses

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.deal_status_collection import DealStatusCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_deal_statuses(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_deal_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_deal_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**DealStatusCollection**](DealStatusCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deal statuses were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_label**
> FoiaLabel get_foia_label(foia_label_id)



Retrieve a single foia label

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_label import FoiaLabel
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_label_id = 56 # int | ID of foia label to retrieve

    try:
        api_response = api_instance.get_foia_label(foia_label_id)
        print("The response of DefaultApi->get_foia_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_foia_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_label_id** | **int**| ID of foia label to retrieve | 

### Return type

[**FoiaLabel**](FoiaLabel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia label was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_labels**
> FoiaLabelCollection get_foia_labels(page=page, per_page=per_page, q=q)



Retrieve some or all foia labels

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_label_collection import FoiaLabelCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_foia_labels(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_foia_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_foia_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**FoiaLabelCollection**](FoiaLabelCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia labels were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_request**
> FoiaRequest get_foia_request(foia_request_id)



Retrieve a single foia request

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_request import FoiaRequest
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_request_id = 56 # int | ID of foia request to retrieve

    try:
        api_response = api_instance.get_foia_request(foia_request_id)
        print("The response of DefaultApi->get_foia_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_foia_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_request_id** | **int**| ID of foia request to retrieve | 

### Return type

[**FoiaRequest**](FoiaRequest.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia request was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_requests**
> FoiaRequestCollection get_foia_requests(page=page, per_page=per_page, q=q)



Retrieve some or all foia requests

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_request_collection import FoiaRequestCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_foia_requests(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_foia_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_foia_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**FoiaRequestCollection**](FoiaRequestCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia requests were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game**
> Game get_game(game_id)



Retrieve a single game

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.game import Game
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    game_id = 56 # int | ID of game to retrieve

    try:
        api_response = api_instance.get_game(game_id)
        print("The response of DefaultApi->get_game:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_game: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **int**| ID of game to retrieve | 

### Return type

[**Game**](Game.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Game was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_games**
> GameCollection get_games(page=page, per_page=per_page, q=q)



Retrieve some or all games

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.game_collection import GameCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_games(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_games: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**GameCollection**](GameCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Games were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_report**
> IncomeReport get_income_report(income_report_id)



Retrieve a single income report

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.income_report import IncomeReport
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    income_report_id = 56 # int | ID of income report to retrieve

    try:
        api_response = api_instance.get_income_report(income_report_id)
        print("The response of DefaultApi->get_income_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_income_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **income_report_id** | **int**| ID of income report to retrieve | 

### Return type

[**IncomeReport**](IncomeReport.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Income report was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_income_reports**
> IncomeReportCollection get_income_reports(page=page, per_page=per_page, q=q)



Retrieve some or all income reports

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.income_report_collection import IncomeReportCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_income_reports(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_income_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_income_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**IncomeReportCollection**](IncomeReportCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Income reports were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_post**
> JobPost get_job_post(job_post_id)

Get a job post

Get a job post

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.job_post import JobPost
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    job_post_id = 56 # int | ID of job post to return

    try:
        # Get a job post
        api_response = api_instance.get_job_post(job_post_id)
        print("The response of DefaultApi->get_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_post_id** | **int**| ID of job post to return | 

### Return type

[**JobPost**](JobPost.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job post was found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_posts**
> JobPostCollection get_job_posts(page=page, per_page=per_page, q=q)

List all job posts

List all job posts

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.job_post_collection import JobPostCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        # List all job posts
        api_response = api_instance.get_job_posts(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_job_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_job_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**JobPostCollection**](JobPostCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job posts were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ncaa_financial_report_status**
> NcaaFinancialReportStatus get_ncaa_financial_report_status(ncaa_financial_report_status_id)



Retrieve a single ncaa financial report status

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.ncaa_financial_report_status import NcaaFinancialReportStatus
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    ncaa_financial_report_status_id = 56 # int | ID of ncaa financial report status to retrieve

    try:
        api_response = api_instance.get_ncaa_financial_report_status(ncaa_financial_report_status_id)
        print("The response of DefaultApi->get_ncaa_financial_report_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ncaa_financial_report_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ncaa_financial_report_status_id** | **int**| ID of ncaa financial report status to retrieve | 

### Return type

[**NcaaFinancialReportStatus**](NcaaFinancialReportStatus.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ncaa financial report status was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ncaa_financial_report_statuses**
> NcaaFinancialReportStatusCollection get_ncaa_financial_report_statuses(page=page, per_page=per_page, q=q)



Retrieve some or all ncaa financial report statuses

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.ncaa_financial_report_status_collection import NcaaFinancialReportStatusCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_ncaa_financial_report_statuses(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_ncaa_financial_report_statuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_ncaa_financial_report_statuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**NcaaFinancialReportStatusCollection**](NcaaFinancialReportStatusCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ncaa financial report statuses were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position**
> Position get_position(position_id)



Retrieve a single position

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.position import Position
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    position_id = 56 # int | ID of position to retrieve

    try:
        api_response = api_instance.get_position(position_id)
        print("The response of DefaultApi->get_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position_id** | **int**| ID of position to retrieve | 

### Return type

[**Position**](Position.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_positions**
> PositionCollection get_positions(page=page, per_page=per_page, q=q)



Retrieve some or all positions

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.position_collection import PositionCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_positions(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_positions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**PositionCollection**](PositionCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Positions were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requested_item**
> RequestedItem get_requested_item(requested_item_id)



Retrieve a single requested item

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.requested_item import RequestedItem
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    requested_item_id = 56 # int | ID of requested item to retrieve

    try:
        api_response = api_instance.get_requested_item(requested_item_id)
        print("The response of DefaultApi->get_requested_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_requested_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_item_id** | **int**| ID of requested item to retrieve | 

### Return type

[**RequestedItem**](RequestedItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested item was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_requested_items**
> RequestedItemCollection get_requested_items(page=page, per_page=per_page, q=q)



Retrieve some or all requested items

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.requested_item_collection import RequestedItemCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_requested_items(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_requested_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_requested_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**RequestedItemCollection**](RequestedItemCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested items were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school**
> School get_school(school_id)



Retrieve a single school

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.school import School
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    school_id = 56 # int | ID of school to retrieve

    try:
        api_response = api_instance.get_school(school_id)
        print("The response of DefaultApi->get_school:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_school: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **int**| ID of school to retrieve | 

### Return type

[**School**](School.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | School was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schools**
> SchoolCollection get_schools(page=page, per_page=per_page, q=q)



Retrieve some or all schools

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.school_collection import SchoolCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_schools(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_schools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_schools: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**SchoolCollection**](SchoolCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schools were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_season**
> Season get_season(season_id)



Retrieve a single season

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.season import Season
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    season_id = 56 # int | ID of season to retrieve

    try:
        api_response = api_instance.get_season(season_id)
        print("The response of DefaultApi->get_season:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_season: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season_id** | **int**| ID of season to retrieve | 

### Return type

[**Season**](Season.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Season was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seasons**
> SeasonCollection get_seasons(page=page, per_page=per_page, q=q)



Retrieve some or all seasons

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.season_collection import SeasonCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_seasons(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_seasons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_seasons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**SeasonCollection**](SeasonCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Seasons were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sport**
> Sport get_sport(sport_id)



Retrieve a single sport

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.sport import Sport
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    sport_id = 56 # int | ID of sport to retrieve

    try:
        api_response = api_instance.get_sport(sport_id)
        print("The response of DefaultApi->get_sport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sport_id** | **int**| ID of sport to retrieve | 

### Return type

[**Sport**](Sport.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sport was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sports**
> SportCollection get_sports(page=page, per_page=per_page, q=q)



Retrieve some or all sports

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.sport_collection import SportCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_sports(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_sports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_sports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**SportCollection**](SportCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sports were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)



Retrieve a single user

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.user import User
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    user_id = 56 # int | ID of user to retrieve

    try:
        api_response = api_instance.get_user(user_id)
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| ID of user to retrieve | 

### Return type

[**User**](User.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User was found |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> UserCollection get_users(page=page, per_page=per_page, q=q)



Retrieve some or all users

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.user_collection import UserCollection
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 100 # int | number of results per page. (optional) (default to 100)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_users(page=page, per_page=per_page, q=q)
        print("The response of DefaultApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 100]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**UserCollection**](UserCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summarizer_post_qa_s3**
> str summarizer_post_qa_s3(summarizer_post_qa_s3_request=summarizer_post_qa_s3_request)

Answer questions over a file from S3

Answer questions a file from S3.

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.summarizer_post_qa_s3_request import SummarizerPostQaS3Request
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    summarizer_post_qa_s3_request = winthrop_client_python.SummarizerPostQaS3Request() # SummarizerPostQaS3Request |  (optional)

    try:
        # Answer questions over a file from S3
        api_response = api_instance.summarizer_post_qa_s3(summarizer_post_qa_s3_request=summarizer_post_qa_s3_request)
        print("The response of DefaultApi->summarizer_post_qa_s3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->summarizer_post_qa_s3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarizer_post_qa_s3_request** | [**SummarizerPostQaS3Request**](SummarizerPostQaS3Request.md)|  | [optional] 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | question response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **summarizer_post_summarize_s3**
> str summarizer_post_summarize_s3(summarizer_post_summarize_s3_request=summarizer_post_summarize_s3_request)

Summarize a file from S3

Summarizes a file from S3.

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.summarizer_post_summarize_s3_request import SummarizerPostSummarizeS3Request
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    summarizer_post_summarize_s3_request = winthrop_client_python.SummarizerPostSummarizeS3Request() # SummarizerPostSummarizeS3Request |  (optional)

    try:
        # Summarize a file from S3
        api_response = api_instance.summarizer_post_summarize_s3(summarizer_post_summarize_s3_request=summarizer_post_summarize_s3_request)
        print("The response of DefaultApi->summarizer_post_summarize_s3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->summarizer_post_summarize_s3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarizer_post_summarize_s3_request** | [**SummarizerPostSummarizeS3Request**](SummarizerPostSummarizeS3Request.md)|  | [optional] 

### Return type

**str**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | summary response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_coach**
> Coach update_coach(coach_id, coach)



Update a coach

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.coach import Coach
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    coach_id = 56 # int | ID of coach to update
    coach = winthrop_client_python.Coach() # Coach | Attributes to update. Currently only supports email, phone, bio, bio_text. Others will be ignored.

    try:
        api_response = api_instance.update_coach(coach_id, coach)
        print("The response of DefaultApi->update_coach:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_coach: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coach_id** | **int**| ID of coach to update | 
 **coach** | [**Coach**](Coach.md)| Attributes to update. Currently only supports email, phone, bio, bio_text. Others will be ignored. | 

### Return type

[**Coach**](Coach.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coach was updated |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_foia_label**
> FoiaLabel update_foia_label(foia_label_id, foia_label)



Update a single foia label

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_label import FoiaLabel
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_label_id = 56 # int | ID of foia label to update
    foia_label = winthrop_client_python.FoiaLabel() # FoiaLabel | Foia label to update

    try:
        api_response = api_instance.update_foia_label(foia_label_id, foia_label)
        print("The response of DefaultApi->update_foia_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_foia_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_label_id** | **int**| ID of foia label to update | 
 **foia_label** | [**FoiaLabel**](FoiaLabel.md)| Foia label to update | 

### Return type

[**FoiaLabel**](FoiaLabel.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia label was updated |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_foia_request**
> FoiaRequest update_foia_request(foia_request_id, foia_request)



Update a single foia request

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_request import FoiaRequest
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    foia_request_id = 56 # int | ID of foia request to update
    foia_request = winthrop_client_python.FoiaRequest() # FoiaRequest | Foia request to update

    try:
        api_response = api_instance.update_foia_request(foia_request_id, foia_request)
        print("The response of DefaultApi->update_foia_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_foia_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foia_request_id** | **int**| ID of foia request to update | 
 **foia_request** | [**FoiaRequest**](FoiaRequest.md)| Foia request to update | 

### Return type

[**FoiaRequest**](FoiaRequest.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia request was updated |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_post**
> JobPost update_job_post(job_post_id, job_post=job_post)

Update a job post

Update a job post

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.job_post import JobPost
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    job_post_id = 56 # int | ID of job post to update
    job_post = winthrop_client_python.JobPost() # JobPost |  (optional)

    try:
        # Update a job post
        api_response = api_instance.update_job_post(job_post_id, job_post=job_post)
        print("The response of DefaultApi->update_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_post_id** | **int**| ID of job post to update | 
 **job_post** | [**JobPost**](JobPost.md)|  | [optional] 

### Return type

[**JobPost**](JobPost.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job post was updated |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_requested_item**
> RequestedItem update_requested_item(requested_item_id, requested_item)



Update a single requested item

### Example

* Api Key Authentication (ApiKey):

```python
import winthrop_client_python
from winthrop_client_python.models.requested_item import RequestedItem
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
    api_instance = winthrop_client_python.DefaultApi(api_client)
    requested_item_id = 56 # int | ID of requested item to update
    requested_item = winthrop_client_python.RequestedItem() # RequestedItem | Requested item to update

    try:
        api_response = api_instance.update_requested_item(requested_item_id, requested_item)
        print("The response of DefaultApi->update_requested_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_requested_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requested_item_id** | **int**| ID of requested item to update | 
 **requested_item** | [**RequestedItem**](RequestedItem.md)| Requested item to update | 

### Return type

[**RequestedItem**](RequestedItem.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested item was updated |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

