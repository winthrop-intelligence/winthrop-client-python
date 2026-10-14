# winthrop_client_python.ContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pending_contract**](ContractsApi.md#create_pending_contract) | **POST** /api/v1/contracts | 
[**delete_pending_contract**](ContractsApi.md#delete_pending_contract) | **DELETE** /api/v1/contracts/{contractId} | 
[**get_contract_history**](ContractsApi.md#get_contract_history) | **GET** /api/v1/contract_history | 
[**publish_pending_contract**](ContractsApi.md#publish_pending_contract) | **POST** /api/v1/contracts/{contractId}/publish | 
[**replace_contract_file**](ContractsApi.md#replace_contract_file) | **PUT** /api/v1/contracts/{contractId}/file | 
[**update_contract**](ContractsApi.md#update_contract) | **PATCH** /api/v1/contracts/{contractId} | 


# **create_pending_contract**
> PendingContractCreated create_pending_contract(coach_id, file, drive_id=drive_id, text=text, contract_terms=contract_terms, change_note=change_note)

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
    change_note = 'change_note_example' # str | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. (optional)

    try:
        api_response = api_instance.create_pending_contract(coach_id, file, drive_id=drive_id, text=text, contract_terms=contract_terms, change_note=change_note)
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
 **change_note** | **str**| Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

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
> delete_pending_contract(contract_id, change_note=change_note)

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
    change_note = 'change_note_example' # str | Optional. Why the record is being deleted, for the internal audit history; stored on every audit version the delete creates and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is deleted. Never returned. (optional)

    try:
        api_instance.delete_pending_contract(contract_id, change_note=change_note)
    except Exception as e:
        print("Exception when calling ContractsApi->delete_pending_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of the pending contract to delete | 
 **change_note** | **str**| Optional. Why the record is being deleted, for the internal audit history; stored on every audit version the delete creates and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is deleted. Never returned. | [optional] 

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
**422** | The contract is not pending, its PDF is used by another record, or change_note is not text or is longer than 500 characters (errors.change_note). Nothing was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_history**
> ContractHistoryCollection get_contract_history(contract_id=contract_id, raw_contract_id=raw_contract_id, coach_id=coach_id, page=page, per_page=per_page)

The change history of a contract and everything under it (WINAD-10638): the contract, its compensations, the
positions linked to them, its verification events and the replacements of its PDF (WINAD-10639, item_type
RawContract, one `file` change with the old and new file), newest first (created_at, then id, descending). Read it
before changing a record: it includes edits staff made in the admin UI since your last run, which have no
change_note and no oauth_application.

Give exactly one of contract_id or raw_contract_id (otherwise 400); coach_id optionally keeps only the
versions recorded for that coach. Each entry names the record (item_type and item_id), the event (create,
update or destroy), every changed field with its old and new value (a create has no old values; a destroy's old
values are the row as it was deleted, so a deleted compensation can be read back), who made the change, the
OAuth app for an API write, when, and the change_note the API write gave.

It exposes editors and internal notes, so it needs the winad_read scope and permission to update the contract
(staff); other users get 403. A contract the caller may not see (a hidden coach's, or a pending one for a
non-manager) is 404.

The history outlives the contract. After a contract is deleted (a pending contract through DELETE
/contracts/{id}, say) contract_id still returns its kept versions, the destroy and its change_note included.
Who may read a deleted contract's history is decided from the row as it was deleted (its destroy version): a
caller who cannot manage coaches gets 404 when the contract was pending, when its coach was hidden or no longer
exists, or when that destroy version was not kept and so the owner is unknown. raw_contract_id does not find
deleted contracts or documents; look those up by contract_id.

A raw_contract_id returns the combined history of every contract that uses the document (a PDF can be shared by
several), merged and ordered newest first. Contracts the caller may not see are left out without a word, and it
is 404 when none is left. coach_id applies across all of them before paging.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.contract_history_collection import ContractHistoryCollection
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
    contract_id = 56 # int | The contract, which may have been deleted since if its versions were kept. Exactly one of contract_id and raw_contract_id is required. (optional)
    raw_contract_id = 56 # int | The document. Returns the combined history of every contract that uses it (live contracts only). Exactly one of contract_id and raw_contract_id is required. (optional)
    coach_id = 56 # int | Keep only the versions recorded for this coach. A version carries the coach its record has after the change, so moving a contract to another coach (WINAD-10639) shows the move under the new coach, while the old coach keeps what was recorded before it. (optional)
    page = 1 # int | results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with `Invalid pagination parameter: page`. (optional) (default to 1)
    per_page = 35 # int | Page size, capped at 100; defaults to 35. (optional) (default to 35)

    try:
        api_response = api_instance.get_contract_history(contract_id=contract_id, raw_contract_id=raw_contract_id, coach_id=coach_id, page=page, per_page=per_page)
        print("The response of ContractsApi->get_contract_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_contract_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| The contract, which may have been deleted since if its versions were kept. Exactly one of contract_id and raw_contract_id is required. | [optional] 
 **raw_contract_id** | **int**| The document. Returns the combined history of every contract that uses it (live contracts only). Exactly one of contract_id and raw_contract_id is required. | [optional] 
 **coach_id** | **int**| Keep only the versions recorded for this coach. A version carries the coach its record has after the change, so moving a contract to another coach (WINAD-10639) shows the move under the new coach, while the old coach keeps what was recorded before it. | [optional] 
 **page** | **int**| results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with &#x60;Invalid pagination parameter: page&#x60;. | [optional] [default to 1]
 **per_page** | **int**| Page size, capped at 100; defaults to 35. | [optional] [default to 35]

### Return type

[**ContractHistoryCollection**](ContractHistoryCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The history, newest first |  -  |
**400** | Not exactly one of contract_id and raw_contract_id, an id that is not a whole number, or a malformed page parameter |  -  |
**401** | Unauthorized |  -  |
**403** | Missing winad_read scope, or not permitted to update contracts |  -  |
**404** | No such contract (neither a live one nor one with kept versions), no contract uses the document, or none is visible to the caller |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_pending_contract**
> PublishedContract publish_pending_contract(contract_id, publish_pending_contract_request)

Publish a pending contract (WINAD-10559). In one transaction, under the coach lock, this sets the contract's dates, writes one compensation per year (creating the later-year positions the coach needs) and sets pending to false. If anything fails nothing is written and the contract stays pending, so the request can be corrected and retried.

The rules are the CSV compensation uploader's: the coach must have a position at each school in the first year listed for it, later years get positions created from it, a school can appear once per coach and year, a yearly or 990 compensation needs a base_salary and an hourly one needs a comment, and a private school's compensation must be 990. A compensation that already exists for the coach, school and year is updated and linked to this contract.

Money is in dollars (a number, or a string such as "$1,234.50" with either no thousands separators or correctly placed ones; "500,00" is refused), converted to cents like the CSV. Flags are JSON booleans. Unknown fields, at the top level or in a row, are refused with 422 rather than ignored. Errors are keyed by attribute for the contract fields (start_on, end_on, at_will, executed_on, expires_on, contingent_change, compensations) and as compensations[n] (n = the row's position in the request, from 0) for a row; row messages name fields by their CSV column, for example "Base Salary". Requires the winad_write scope and a manage-level user.


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

# **replace_contract_file**
> ContractFileReplaced replace_contract_file(contract_id, file, change_note=change_note)

Replace the PDF of an existing contract, pending or published (WINAD-10639). Send multipart/form-data with the new PDF as `file` and an optional `change_note`. The old file (and its OCR copy) is replaced, not kept as an attachment, the stored text is cleared and OCR runs again, as for an upload in the admin UI. The contract's structured terms are not touched (they read as stale against the new text).

The file must really be a PDF (its bytes are checked, not its name). The replacement is recorded in the change history (GET /contract_history) as a RawContract entry with a `file` change, the acting user, the API client and the change_note. A PDF that another record also uses is refused. The swap takes the locks of a coach move (the contract's coach, then the contract, then its RawContract), so it never deadlocks with a move or a verification, and the change history entry names the coach the contract has when the file is swapped. Requires winad_write, a manage-level user with a user-backed OAuth token.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.contract_file_replaced import ContractFileReplaced
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
    contract_id = 56 # int | ID of the contract whose PDF is replaced
    file = None # bytearray | The new contract PDF
    change_note = 'change_note_example' # str | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. (optional)

    try:
        api_response = api_instance.replace_contract_file(contract_id, file, change_note=change_note)
        print("The response of ContractsApi->replace_contract_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->replace_contract_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **int**| ID of the contract whose PDF is replaced | 
 **file** | **bytearray**| The new contract PDF | 
 **change_note** | **str**| Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

### Return type

[**ContractFileReplaced**](ContractFileReplaced.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file was replaced and OCR queued |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope, not a manage-level user, or a client-credentials token with no user) |  -  |
**404** | Not Found (no such contract, a hidden coach&#39;s, or a pending one for a non-manager), or the contract was deleted while the request ran |  -  |
**422** | Missing or non-PDF file, a contract with no PDF record, a PDF another record uses, or an invalid change_note (errors.change_note). The old file is untouched. |  -  |
**409** | The contract was moved to another coach again and again while the request waited for its locks (errors.contract). Nothing was written; reload the contract and retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract**
> Contract update_contract(contract_id, update_contract_request)

Edit a published contract's start_on, end_on, executed_on, expires_on, at_will, contingent_change and coach_id (WINAD-10631, WINAD-10639). Only supplied fields change; linked compensations are unchanged. Pending contracts are published, not edited (use POST /contracts/{contractId}/publish).
Dates must be YYYY-MM-DD and flags JSON true or false (the same rules as publish). Setting at_will true requires end_on null; send both fields to clear a stored end date. The at-will/end-date rule is checked only when either field is supplied, allowing start-only corrections on legacy rows. end_on, executed_on and expires_on can be cleared with null.
coach_id moves the contract to another coach, in the same transaction as the other fields. A move is refused with 422 (errors.coach_id) when the coach does not exist or is not visible to the caller, or while any compensation, any position of those compensations, any verification event or any earned incentive still links to the contract (an earned incentive links through its raw_contract_id or its ended_by_contract_id being the contract's RawContract): the body then also lists linked_compensation_ids, linked_position_ids, linked_verification_ids and linked_earned_incentive_ids, and nothing is written. Never move those rows from the API; a person unlinks or moves them first. Sending the coach it already has is a no-op.
A move also files the contract's PDF under the new coach's current school (raw_contracts.school_id, the school the pending upload sets, null when the new coach has no current position), in the same transaction. A PDF that another record also uses (another contract, a game contract, a deal and so on) or a financial report is left unchanged, and so is the school when the move is refused or the coach is unchanged. The school change is a RawContract entry in GET /contract_history, under the new coach, with the change_note and the user, and the response body is unchanged.
Each change creates a PaperTrail version with the authenticated user (whodunnit) and the optional top-level change_note (at most 500 characters). Identical values are a no-op and create no version, so no note is stored. Requires winad_write and a manage-level user with a user-backed OAuth token.
Every edit takes the locks of a coach move (the contract's coach, the coach it moves to, then the contract), so it never overlaps a move or a verification being recorded for the contract. A request that waits for them sees the contract as the other write left it. Only a contract that keeps moving while the locks are taken is refused with 409.


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
**422** | Pending contract, no updatable fields, unknown or mis-typed field, change_note that is not a string (errors.change_note), bad date, at_will with end_on, missing required date, start after end, or a refused coach move (errors.coach_id, with the linked_*_ids lists, earned incentives included). Nothing was written. |  -  |
**409** | The contract was moved to another coach again and again while the request waited for its locks (errors.contract). Nothing was written; reload the contract and retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

