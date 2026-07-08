# winthrop_client_python.IntercollegiateApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_news_feeds**](IntercollegiateApi.md#create_news_feeds) | **POST** /wi_jobs/news_feeds | 
[**get_job_post**](IntercollegiateApi.md#get_job_post) | **GET** /wi_jobs/job_posts/{jobPostId} | 
[**get_job_post_interest_leads**](IntercollegiateApi.md#get_job_post_interest_leads) | **GET** /wi_jobs/job_post_interest_leads | 
[**get_job_post_salary_benchmark**](IntercollegiateApi.md#get_job_post_salary_benchmark) | **GET** /wi_jobs/job_posts/salary_benchmark | 
[**get_job_posts**](IntercollegiateApi.md#get_job_posts) | **GET** /wi_jobs/job_posts | 
[**get_news_feeds**](IntercollegiateApi.md#get_news_feeds) | **GET** /wi_jobs/news_feeds | 


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

# **get_job_post_interest_leads**
> JobPostInterestLeadCollection get_job_post_interest_leads(var_date=var_date, submitted_after=submitted_after, submitted_before=submitted_before, page=page, per_page=per_page)

Retrieve currently active "I'm interested" job-post submissions (leads) for outreach. Only active interest rows are returned; if a candidate undoes their interest in the UI the row is deleted and will not appear in any subsequent response, including for the same date/window.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job_post_interest_lead_collection import JobPostInterestLeadCollection
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
    var_date = 'Mon Jun 22 00:00:00 UTC 2026' # date | Restrict to interests submitted on this calendar day (application time zone). Format YYYY-MM-DD. May be combined with the submitted_after/submitted_before bounds. (optional)
    submitted_after = '2026-06-22T00:00Z' # datetime | Only include interests submitted at or after this timestamp (ISO 8601). (optional)
    submitted_before = '2026-06-22T23:59:59.999Z' # datetime | Only include interests submitted at or before this timestamp (ISO 8601). (optional)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    per_page = 20 # int | number of results per page. (optional) (default to 20)

    try:
        api_response = api_instance.get_job_post_interest_leads(var_date=var_date, submitted_after=submitted_after, submitted_before=submitted_before, page=page, per_page=per_page)
        print("The response of IntercollegiateApi->get_job_post_interest_leads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->get_job_post_interest_leads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **date**| Restrict to interests submitted on this calendar day (application time zone). Format YYYY-MM-DD. May be combined with the submitted_after/submitted_before bounds. | [optional] 
 **submitted_after** | **datetime**| Only include interests submitted at or after this timestamp (ISO 8601). | [optional] 
 **submitted_before** | **datetime**| Only include interests submitted at or before this timestamp (ISO 8601). | [optional] 
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. | [optional] [default to 20]

### Return type

[**JobPostInterestLeadCollection**](JobPostInterestLeadCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Interest leads were found |  -  |
**400** | Invalid request — a supplied date/submitted_after/submitted_before value could not be parsed. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_post_salary_benchmark**
> JobPostSalaryBenchmark get_job_post_salary_benchmark(role_query=role_query, department=department, sport=sport, conference=conference, division=division, school_query=school_query, peer_set=peer_set, date_range_start=date_range_start, date_range_end=date_range_end, salary_basis=salary_basis, response_format=response_format)

Benchmark recent posted salary ranges for comparable Intercollegiate job posts. This endpoint uses posted job salary fields only and does not use executed WinAD compensation data.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.job_post_salary_benchmark import JobPostSalaryBenchmark
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
    role_query = 'role_query_example' # str | Natural-language role/title query, such as athletics HR or Assistant AD Marketing. (optional)
    department = 'department_example' # str | Department filter, such as Human Resources, Marketing, or Business Office. (optional)
    sport = 'sport_example' # str | Sport filter. (optional)
    conference = 'conference_example' # str | Conference name or nickname filter, such as SEC. (optional)
    division = 'division_example' # str | Division or subdivision filter, such as Division I, DI, FBS, or Power 4. (optional)
    school_query = 'school_query_example' # str | School name, short name, local ID, or WinAD ID filter. (optional)
    peer_set = ['peer_set_example'] # List[str] | Explicit peer school names or IDs. May be supplied multiple times or comma-separated. (optional)
    date_range_start = '2013-10-20' # date | Start of the posted_at date window. Defaults to six months ago. (optional)
    date_range_end = '2013-10-20' # date | End of the posted_at date window. Defaults to today. (optional)
    salary_basis = posted_range # str | Salary basis requested for the benchmark. (optional) (default to posted_range)
    response_format = concise # str | Concise returns up to five representative posts; detailed returns up to ten. (optional) (default to concise)

    try:
        api_response = api_instance.get_job_post_salary_benchmark(role_query=role_query, department=department, sport=sport, conference=conference, division=division, school_query=school_query, peer_set=peer_set, date_range_start=date_range_start, date_range_end=date_range_end, salary_basis=salary_basis, response_format=response_format)
        print("The response of IntercollegiateApi->get_job_post_salary_benchmark:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercollegiateApi->get_job_post_salary_benchmark: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_query** | **str**| Natural-language role/title query, such as athletics HR or Assistant AD Marketing. | [optional] 
 **department** | **str**| Department filter, such as Human Resources, Marketing, or Business Office. | [optional] 
 **sport** | **str**| Sport filter. | [optional] 
 **conference** | **str**| Conference name or nickname filter, such as SEC. | [optional] 
 **division** | **str**| Division or subdivision filter, such as Division I, DI, FBS, or Power 4. | [optional] 
 **school_query** | **str**| School name, short name, local ID, or WinAD ID filter. | [optional] 
 **peer_set** | [**List[str]**](str.md)| Explicit peer school names or IDs. May be supplied multiple times or comma-separated. | [optional] 
 **date_range_start** | **date**| Start of the posted_at date window. Defaults to six months ago. | [optional] 
 **date_range_end** | **date**| End of the posted_at date window. Defaults to today. | [optional] 
 **salary_basis** | **str**| Salary basis requested for the benchmark. | [optional] [default to posted_range]
 **response_format** | **str**| Concise returns up to five representative posts; detailed returns up to ten. | [optional] [default to concise]

### Return type

[**JobPostSalaryBenchmark**](JobPostSalaryBenchmark.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Posted salary benchmark packet. |  -  |
**400** | Invalid request parameters. |  -  |
**401** | Unauthorized |  -  |
**403** | Insufficient scope |  -  |

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

