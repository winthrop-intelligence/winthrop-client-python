# winthrop_client_python.ContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pending_contract**](ContractsApi.md#create_pending_contract) | **POST** /api/v1/contracts | 
[**delete_pending_contract**](ContractsApi.md#delete_pending_contract) | **DELETE** /api/v1/contracts/{contractId} | 
[**publish_pending_contract**](ContractsApi.md#publish_pending_contract) | **POST** /api/v1/contracts/{contractId}/publish | 
[**update_contract**](ContractsApi.md#update_contract) | **PATCH** /api/v1/contracts/{contractId} | 


# **create_pending_contract**
> PendingContractCreated create_pending_contract(coach_id, file, drive_id=drive_id, text=text, contract_terms=contract_terms)

Upload a PDF to a coach as a pending contract. Creates a RawContract with the file attached and a Contract with pending true (no dates) in one transaction; nothing is created if the request is refused. Requires the winad_write scope and a manage-level user. The file must really be a PDF (its bytes are checked, not its name).

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.pending_contract_created import PendingContractCreated
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
    api_instance = winthrop_client_python.ContractsApi(api_client)
    coach_id = 56 # int | The coach the contract is filed on
    file = None # bytearray | The contract PDF
    drive_id = 'drive_id_example' # str | Optional Google Drive id; must be unique for the coach (optional)
    text = 'text_example' # str | Optional Mistral markdown already produced for this PDF, pages separated by a form feed line (\\\"\\\\n\\\\f\\\\n\\\"). When present it is stored as the contract text and no automatic OCR is queued; when absent one automatic OCR job is queued. (optional)
    contract_terms = 'contract_terms_example' # str | Optional structured terms read from the contract, as a JSON-encoded ContractTerms object (see PATCH /raw_contracts/{id}/contract_terms). Stored on the RawContract in the same transaction; an invalid document refuses the upload with errors keyed contract_terms, contract_terms.schema, contract_terms.source.run_id, and so on. Accepted from service (client-credentials) tokens like the rest of the upload; the audit version then records no person. (optional)

    try:
        api_response = api_instance.create_pending_contract(coach_id, file, drive_id=drive_id, text=text, contract_terms=contract_terms)
        print("The response of ContractsApi->create_pending_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_pending_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coach_id** | **int**| The coach the contract is filed on | 
 **file** | **bytearray**| The contract PDF | 
 **drive_id** | **str**| Optional Google Drive id; must be unique for the coach | [optional] 
 **text** | **str**| Optional Mistral markdown already produced for this PDF, pages separated by a form feed line (\\\&quot;\\\\n\\\\f\\\\n\\\&quot;). When present it is stored as the contract text and no automatic OCR is queued; when absent one automatic OCR job is queued. | [optional] 
 **contract_terms** | **str**| Optional structured terms read from the contract, as a JSON-encoded ContractTerms object (see PATCH /raw_contracts/{id}/contract_terms). Stored on the RawContract in the same transaction; an invalid document refuses the upload with errors keyed contract_terms, contract_terms.schema, contract_terms.source.run_id, and so on. Accepted from service (client-credentials) tokens like the rest of the upload; the audit version then records no person. | [optional] 

### Return type

[**PendingContractCreated**](PendingContractCreated.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pending contract was created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to create contracts) |  -  |
**422** | The upload was refused (unknown coach, missing or non-PDF file, duplicate drive_id, invalid contract_terms). Nothing was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pending_contract**
> delete_pending_contract(contract_id)

Delete a contract, only while it is pending. Also deletes its RawContract and the stored PDF, so no file is left behind. A published contract, or a PDF that another record still uses, is refused. Requires the winad_write scope and a manage-level user.

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
    api_instance = winthrop_client_python.ContractsApi(api_client)
    contract_id = 56 # int | ID of the pending contract to delete

    try:
        api_instance.delete_pending_contract(contract_id)
    except Exception as e:
        print("Exception when calling ContractsApi->delete_pending_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of the pending contract to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The pending contract, its RawContract and its file were deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to delete contracts) |  -  |
**404** | Not Found |  -  |
**422** | The contract is not pending, or its PDF is used by another record. Nothing was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_pending_contract**
> PublishedContract publish_pending_contract(contract_id, publish_pending_contract_request)

Publish a pending contract (WINAD-10559). In one transaction, under the coach lock, this sets the contract's dates, writes one compensation per year (creating the later-year positions the coach needs) and sets pending to false. If anything fails nothing is written and the contract stays pending, so the request can be corrected and retried.

The rules are the CSV compensation uploader's: the coach must have a position at each school in the first year listed for it, later years get positions created from it, a school can appear once per coach and year, a yearly or 990 compensation needs a base_salary and an hourly one needs a comment, and a private school's compensation must be 990. A compensation that already exists for the coach, school and year is updated and linked to this contract.

Money is in dollars (a number, or a string such as "$1,234.50" with either no thousands separators or correctly placed ones; "500,00" is refused), converted to cents like the CSV. Flags are JSON booleans. Unknown fields, at the top level or in a row, are refused with 422 rather than ignored. Errors are keyed by attribute for the contract fields (start_on, end_on, at_will, executed_on, compensations) and as compensations[n] (n = the row's position in the request, from 0) for a row; row messages name fields by their CSV column, for example "Base Salary". Requires the winad_write scope and a manage-level user.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.publish_pending_contract_request import PublishPendingContractRequest
from winthrop_client_python.models.published_contract import PublishedContract
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
    api_instance = winthrop_client_python.ContractsApi(api_client)
    contract_id = 56 # int | ID of the pending contract to publish
    publish_pending_contract_request = winthrop_client_python.PublishPendingContractRequest() # PublishPendingContractRequest | 

    try:
        api_response = api_instance.publish_pending_contract(contract_id, publish_pending_contract_request)
        print("The response of ContractsApi->publish_pending_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->publish_pending_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of the pending contract to publish | 
 **publish_pending_contract_request** | [**PublishPendingContractRequest**](PublishPendingContractRequest.md)|  | 

### Return type

[**PublishedContract**](PublishedContract.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contract was published and its compensations written |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to update contracts) |  -  |
**404** | Not Found |  -  |
**422** | The contract is not pending, or the dates or a compensation row were refused. Nothing was written and the contract is still pending. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract**
> Contract update_contract(contract_id, update_contract_request)

Edit a published contract's start_on, end_on and at_will (WINAD-10631). Only supplied fields change; linked compensations are unchanged. Pending contracts are published, not edited (use POST /contracts/{contractId}/publish).
Dates must be YYYY-MM-DD. Setting at_will true requires end_on null; send both fields to clear a stored end date. The at-will/end-date rule is checked only when either field is supplied, allowing start-only corrections on legacy rows.
Each change creates a PaperTrail version with the authenticated user (whodunnit) and the optional top-level change_note. Identical values are a no-op and create no version, so no note is stored. Requires winad_write and a manage-level user with a user-backed OAuth token.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.contract import Contract
from winthrop_client_python.models.update_contract_request import UpdateContractRequest
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
    api_instance = winthrop_client_python.ContractsApi(api_client)
    contract_id = 56 # int | ID of the published contract to update
    update_contract_request = winthrop_client_python.UpdateContractRequest() # UpdateContractRequest | 

    try:
        api_response = api_instance.update_contract(contract_id, update_contract_request)
        print("The response of ContractsApi->update_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->update_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of the published contract to update | 
 **update_contract_request** | [**UpdateContractRequest**](UpdateContractRequest.md)|  | 

### Return type

[**Contract**](Contract.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated contract, re-read from the database |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope, not a manage-level user, or a client-credentials token with no user: Updating contracts requires a user-backed OAuth token) |  -  |
**404** | Not Found |  -  |
**422** | Pending contract, no updatable fields, unknown or mis-typed field, change_note that is not a string (errors.change_note), bad date, at_will with end_on, missing required date, or start after end. Nothing was written. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

