# winthrop_client_python.IntercollegiateApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_post**](IntercollegiateApi.md#create_job_post) | **POST** /wi_jobs/job_posts | 
[**create_news_feeds**](IntercollegiateApi.md#create_news_feeds) | **POST** /wi_jobs/news_feeds | 
[**delete_job_post**](IntercollegiateApi.md#delete_job_post) | **DELETE** /wi_jobs/job_posts/{jobPostId} | 
[**get_job_post**](IntercollegiateApi.md#get_job_post) | **GET** /wi_jobs/job_posts/{jobPostId} | 
[**get_job_posts**](IntercollegiateApi.md#get_job_posts) | **GET** /wi_jobs/job_posts | 
[**get_news_feeds**](IntercollegiateApi.md#get_news_feeds) | **GET** /wi_jobs/news_feeds | 
[**update_job_post**](IntercollegiateApi.md#update_job_post) | **PATCH** /wi_jobs/job_posts/{jobPostId} | 


# **create_job_post**
> Job create_job_post(remote_job_post)

Create or sync a remote job post

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job import Job
from winthrop_client_python.models.remote_job_post import RemoteJobPost
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
    api_instance = winthrop_client_python.IntercollegiateApi(api_client)
    remote_job_post = winthrop_client_python.RemoteJobPost() # RemoteJobPost | 

    try:
        api_response = api_instance.create_job_post(remote_job_post)
        print("The response of IntercollegiateApi->create_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->create_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_job_post** | [**RemoteJobPost**](RemoteJobPost.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Job post was created or synced |  -  |
**204** | Stale sync payload was ignored |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Invalid job post payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_news_feeds**
> NewsFeed create_news_feeds(news_feed=news_feed)

Create news feed

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.news_feed import NewsFeed
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
    api_instance = winthrop_client_python.IntercollegiateApi(api_client)
    news_feed = winthrop_client_python.NewsFeed() # NewsFeed |  (optional)

    try:
        api_response = api_instance.create_news_feeds(news_feed=news_feed)
        print("The response of IntercollegiateApi->create_news_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->create_news_feeds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **news_feed** | [**NewsFeed**](NewsFeed.md)|  | [optional] 

### Return type

[**NewsFeed**](NewsFeed.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | News Feed was create |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_post**
> delete_job_post(job_post_id, updated_at)

Delete a synced remote job post

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with winthrop_client_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = winthrop_client_python.IntercollegiateApi(api_client)
    job_post_id = 56 # int | Remote ID of job post to delete
    updated_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp of the remote operation being synced.

    try:
        api_instance.delete_job_post(job_post_id, updated_at)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->delete_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_post_id** | **int**| Remote ID of job post to delete | 
 **updated_at** | **datetime**| Timestamp of the remote operation being synced. | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Job post was deleted or was already absent |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Invalid delete payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_post**
> Job get_job_post(job_post_id)

Retrieve a job post by ID

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job import Job
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
    api_instance = winthrop_client_python.IntercollegiateApi(api_client)
    job_post_id = 56 # int | ID of job post to return

    try:
        api_response = api_instance.get_job_post(job_post_id)
        print("The response of IntercollegiateApi->get_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->get_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_post_id** | **int**| ID of job post to return | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job Post was found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_posts**
> JobCollection get_job_posts(page=page, per_page=per_page, q=q)

Retrieve some or all active jobs

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job_collection import JobCollection
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
    api_instance = winthrop_client_python.IntercollegiateApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 20 # int | number of results per page. (optional) (default to 20)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_job_posts(page=page, per_page=per_page, q=q)
        print("The response of IntercollegiateApi->get_job_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->get_job_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 20]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**JobCollection**](JobCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Jobs were found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_news_feeds**
> NewsFeedCollection get_news_feeds()

Retrieve news feed

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.news_feed_collection import NewsFeedCollection
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
    api_instance = winthrop_client_python.IntercollegiateApi(api_client)

    try:
        api_response = api_instance.get_news_feeds()
        print("The response of IntercollegiateApi->get_news_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->get_news_feeds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NewsFeedCollection**](NewsFeedCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | News Feed were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_post**
> Job update_job_post(job_post_id, remote_job_post)

Update or sync a remote job post

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job import Job
from winthrop_client_python.models.remote_job_post import RemoteJobPost
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
    api_instance = winthrop_client_python.IntercollegiateApi(api_client)
    job_post_id = 56 # int | Remote ID of job post to update
    remote_job_post = winthrop_client_python.RemoteJobPost() # RemoteJobPost | 

    try:
        api_response = api_instance.update_job_post(job_post_id, remote_job_post)
        print("The response of IntercollegiateApi->update_job_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->update_job_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_post_id** | **int**| Remote ID of job post to update | 
 **remote_job_post** | [**RemoteJobPost**](RemoteJobPost.md)|  | 

### Return type

[**Job**](Job.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job post was updated or synced |  -  |
**204** | Stale sync payload was ignored |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Invalid job post payload |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

