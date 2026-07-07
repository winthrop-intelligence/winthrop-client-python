# winthrop_client_python.ReportingApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coach_contract_requests**](ReportingApi.md#get_coach_contract_requests) | **GET** /api/v1/reports/coach_contract_requests | 
[**get_coach_history**](ReportingApi.md#get_coach_history) | **GET** /api/v1/reports/coach_history | 
[**get_conferenceships**](ReportingApi.md#get_conferenceships) | **GET** /api/v1/reports/conferenceships | 
[**get_foia_details**](ReportingApi.md#get_foia_details) | **GET** /api/v1/reports/foia_details | 
[**get_foia_follow_up_report**](ReportingApi.md#get_foia_follow_up_report) | **GET** /api/v1/reports/foia_follow_up_report | 
[**get_foia_requested_item_status_breakdown**](ReportingApi.md#get_foia_requested_item_status_breakdown) | **GET** /api/v1/reports/foia_requested_item_status_breakdown | 
[**get_foia_requested_item_status_transitions**](ReportingApi.md#get_foia_requested_item_status_transitions) | **GET** /api/v1/reports/foia_requested_item_status_transitions | 
[**get_games**](ReportingApi.md#get_games) | **GET** /api/v1/reports/games | 
[**get_invoices**](ReportingApi.md#get_invoices) | **GET** /api/v1/reports/invoices | 
[**get_school_contract_requests**](ReportingApi.md#get_school_contract_requests) | **GET** /api/v1/reports/school_contract_requests | 
[**get_schools_financials_qc**](ReportingApi.md#get_schools_financials_qc) | **GET** /api/v1/financials_qc | 
[**get_subscriptions**](ReportingApi.md#get_subscriptions) | **GET** /api/v1/reports/subscriptions | 


# **get_coach_contract_requests**
> object get_coach_contract_requests(page=page, q=q)

Retrieve some or all coach contract requests

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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_coach_contract_requests(page=page, q=q)
        print("The response of ReportingApi->get_coach_contract_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_coach_contract_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coach contract requests were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coach_history**
> object get_coach_history(page=page, q=q)

Retrieve some or all coach history

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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_coach_history(page=page, q=q)
        print("The response of ReportingApi->get_coach_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_coach_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Coach history was found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conferenceships**
> object get_conferenceships(page=page, q=q)

Retrieve some or all conferenceships

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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_conferenceships(page=page, q=q)
        print("The response of ReportingApi->get_conferenceships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_conferenceships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conferenceships were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_details**
> object get_foia_details(page=page, q=q)

Retrieve some or all foia details

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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_foia_details(page=page, q=q)
        print("The response of ReportingApi->get_foia_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_foia_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Foia details were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_follow_up_report**
> FoiaFollowUpReportResponse get_foia_follow_up_report(scope, page=page, per_page=per_page, sort_by=sort_by, foia_label_id=foia_label_id, school_id=school_id, state=state, follow_up_date_lte=follow_up_date_lte, include_not_due=include_not_due, show_processed_today=show_processed_today, include_direct_contact=include_direct_contact)

Retrieve read-only FOIA follow-up rows for Codex follow-up drafting and FOIA freshness dashboards

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_follow_up_report_response import FoiaFollowUpReportResponse
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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    scope = 'scope_example' # str | 
    page = 1 # int | Results page to retrieve. (optional) (default to 1)
    per_page = 40 # int | Number of rows per page. Values above 200 are capped at 200. (optional) (default to 40)
    sort_by = follow_up_date_asc # str | Sort field with optional _asc or _desc suffix. (optional) (default to follow_up_date_asc)
    foia_label_id = 56 # int |  (optional)
    school_id = 56 # int |  (optional)
    state = 'state_example' # str | School state id, abbreviation, or display name. (optional)
    follow_up_date_lte = '2013-10-20' # date |  (optional)
    include_not_due = False # bool |  (optional) (default to False)
    show_processed_today = false # str |  (optional) (default to false)
    include_direct_contact = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_foia_follow_up_report(scope, page=page, per_page=per_page, sort_by=sort_by, foia_label_id=foia_label_id, school_id=school_id, state=state, follow_up_date_lte=follow_up_date_lte, include_not_due=include_not_due, show_processed_today=show_processed_today, include_direct_contact=include_direct_contact)
        print("The response of ReportingApi->get_foia_follow_up_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_foia_follow_up_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **page** | **int**| Results page to retrieve. | [optional] [default to 1]
 **per_page** | **int**| Number of rows per page. Values above 200 are capped at 200. | [optional] [default to 40]
 **sort_by** | **str**| Sort field with optional _asc or _desc suffix. | [optional] [default to follow_up_date_asc]
 **foia_label_id** | **int**|  | [optional] 
 **school_id** | **int**|  | [optional] 
 **state** | **str**| School state id, abbreviation, or display name. | [optional] 
 **follow_up_date_lte** | **date**|  | [optional] 
 **include_not_due** | **bool**|  | [optional] [default to False]
 **show_processed_today** | **str**|  | [optional] [default to false]
 **include_direct_contact** | **bool**|  | [optional] [default to False]

### Return type

[**FoiaFollowUpReportResponse**](FoiaFollowUpReportResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FOIA follow-up report rows were found |  -  |
**400** | Invalid report parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_requested_item_status_breakdown**
> FoiaRequestedItemStatusBreakdownResponse get_foia_requested_item_status_breakdown(group_by=group_by, period=period, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, foia_label_id=foia_label_id, school_id=school_id, state=state, include_direct_contact=include_direct_contact)

Retrieve read-only grouped requested-item status counts for FOIA freshness reporting widgets

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_requested_item_status_breakdown_response import FoiaRequestedItemStatusBreakdownResponse
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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    group_by = 'updated_period,requestable_type' # str | Comma-separated grouping dimensions. Defaults to both dimensions. (optional) (default to 'updated_period,requestable_type')
    period = day # str | Calendar bucket size for the updated_period dimension. Weeks are ISO weeks starting Monday. (optional) (default to day)
    updated_at_gte = '2013-10-20' # date | Include items updated on or after this date. (optional)
    updated_at_lte = '2013-10-20' # date | Include items updated on or before this date. (optional)
    foia_label_id = 56 # int |  (optional)
    school_id = 56 # int |  (optional)
    state = 'state_example' # str | School state id, abbreviation, or display name. (optional)
    include_direct_contact = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.get_foia_requested_item_status_breakdown(group_by=group_by, period=period, updated_at_gte=updated_at_gte, updated_at_lte=updated_at_lte, foia_label_id=foia_label_id, school_id=school_id, state=state, include_direct_contact=include_direct_contact)
        print("The response of ReportingApi->get_foia_requested_item_status_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_foia_requested_item_status_breakdown: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_by** | **str**| Comma-separated grouping dimensions. Defaults to both dimensions. | [optional] [default to &#39;updated_period,requestable_type&#39;]
 **period** | **str**| Calendar bucket size for the updated_period dimension. Weeks are ISO weeks starting Monday. | [optional] [default to day]
 **updated_at_gte** | **date**| Include items updated on or after this date. | [optional] 
 **updated_at_lte** | **date**| Include items updated on or before this date. | [optional] 
 **foia_label_id** | **int**|  | [optional] 
 **school_id** | **int**|  | [optional] 
 **state** | **str**| School state id, abbreviation, or display name. | [optional] 
 **include_direct_contact** | **bool**|  | [optional] [default to False]

### Return type

[**FoiaRequestedItemStatusBreakdownResponse**](FoiaRequestedItemStatusBreakdownResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Grouped requested-item status counts were found |  -  |
**400** | Invalid report parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_foia_requested_item_status_transitions**
> FoiaRequestedItemStatusTransitionsResponse get_foia_requested_item_status_transitions(changed_at_gte, changed_at_lte=changed_at_lte, foia_label_id=foia_label_id, school_id=school_id, requestable_type=requestable_type, page=page, per_page=per_page)

Retrieve read-only requested-item status transition history (into received or not_available) sourced from audit versions, for items-received FOIA freshness reporting. Rows are transition events, so one item can appear multiple times. Label, school, and requestable fields reflect each item's current associations rather than the values at transition time, and only items on active requests with unarchived labels are included. Status changes written without callbacks are not captured in the audit history and do not appear.

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.foia_requested_item_status_transitions_response import FoiaRequestedItemStatusTransitionsResponse
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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    changed_at_gte = 'changed_at_gte_example' # str | Include transitions on or after this ISO-8601 date or datetime. Date-only values start at the beginning of the day.
    changed_at_lte = 'changed_at_lte_example' # str | Include transitions on or before this ISO-8601 date or datetime. Date-only values run through the end of the day. Defaults to now; the window may span at most 366 days. (optional)
    foia_label_id = 56 # int |  (optional)
    school_id = 56 # int |  (optional)
    requestable_type = 'requestable_type_example' # str |  (optional)
    page = 1 # int |  (optional) (default to 1)
    per_page = 40 # int | Values above the maximum are capped. (optional) (default to 40)

    try:
        api_response = api_instance.get_foia_requested_item_status_transitions(changed_at_gte, changed_at_lte=changed_at_lte, foia_label_id=foia_label_id, school_id=school_id, requestable_type=requestable_type, page=page, per_page=per_page)
        print("The response of ReportingApi->get_foia_requested_item_status_transitions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_foia_requested_item_status_transitions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changed_at_gte** | **str**| Include transitions on or after this ISO-8601 date or datetime. Date-only values start at the beginning of the day. | 
 **changed_at_lte** | **str**| Include transitions on or before this ISO-8601 date or datetime. Date-only values run through the end of the day. Defaults to now; the window may span at most 366 days. | [optional] 
 **foia_label_id** | **int**|  | [optional] 
 **school_id** | **int**|  | [optional] 
 **requestable_type** | **str**|  | [optional] 
 **page** | **int**|  | [optional] [default to 1]
 **per_page** | **int**| Values above the maximum are capped. | [optional] [default to 40]

### Return type

[**FoiaRequestedItemStatusTransitionsResponse**](FoiaRequestedItemStatusTransitionsResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested-item status transitions were found |  -  |
**400** | Invalid report parameters |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_games**
> object get_games(page=page, q=q)

Retrieve some or all games

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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_games(page=page, q=q)
        print("The response of ReportingApi->get_games:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_games: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Games were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> InvoiceReportResult get_invoices(page=page, q=q)

Retrieve some or all client invoices

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.invoice_report_result import InvoiceReportResult
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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_invoices(page=page, q=q)
        print("The response of ReportingApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**InvoiceReportResult**](InvoiceReportResult.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoices were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_school_contract_requests**
> object get_school_contract_requests(page=page, q=q)

Retrieve some or all school contract requests

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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_school_contract_requests(page=page, q=q)
        print("The response of ReportingApi->get_school_contract_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_school_contract_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | School contract requests were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schools_financials_qc**
> FinancialQc get_schools_financials_qc(page=page, q=q)

Retrieve schools with thier financials qc

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.financial_qc import FinancialQc
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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_schools_financials_qc(page=page, q=q)
        print("The response of ReportingApi->get_schools_financials_qc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_schools_financials_qc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

[**FinancialQc**](FinancialQc.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | some schools with thier financials qc report |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> object get_subscriptions(page=page, q=q)

Retrieve subscriptions

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
    api_instance = winthrop_client_python.ReportingApi(api_client)
    page = 1 # int | results page to retrieve. (optional) (default to 1)
    q = None # object | Ransack query (optional)

    try:
        api_response = api_instance.get_subscriptions(page=page, q=q)
        print("The response of ReportingApi->get_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->get_subscriptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. | [optional] [default to 1]
 **q** | [**object**](.md)| Ransack query | [optional] 

### Return type

**object**

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | some subscriptions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

