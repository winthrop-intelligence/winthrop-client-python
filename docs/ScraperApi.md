# winthrop_client_python.ScraperApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_scrapers**](ScraperApi.md#list_scrapers) | **GET** /ondemand-scrapers/ | List all available scrapers
[**run_scraper**](ScraperApi.md#run_scraper) | **POST** /ondemand-scrapers/run/{command} | Run a scraper


# **list_scrapers**
> List[Scraper] list_scrapers()

List all available scrapers

### Example

* Api Key Authentication (ApiKey):

```python
import time
import os
import winthrop_client_python
from winthrop_client_python.models.scraper import Scraper
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
    api_instance = winthrop_client_python.ScraperApi(api_client)

    try:
        # List all available scrapers
        api_response = api_instance.list_scrapers()
        print("The response of ScraperApi->list_scrapers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScraperApi->list_scrapers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Scraper]**](Scraper.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of available scrapers |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_scraper**
> run_scraper(command)

Run a scraper

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
    api_instance = winthrop_client_python.ScraperApi(api_client)
    command = 'command_example' # str | The name of the scraper to run

    try:
        # Run a scraper
        api_instance.run_scraper(command)
    except Exception as e:
        print("Exception when calling ScraperApi->run_scraper: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**| The name of the scraper to run | 

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
**200** | The scraper was successfully started |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

