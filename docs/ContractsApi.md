# winthrop_client_python.ContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contract_direct_upload**](ContractsApi.md#create_contract_direct_upload) | **POST** /api/v1/contracts/direct_uploads | 
[**create_pending_contract**](ContractsApi.md#create_pending_contract) | **POST** /api/v1/contracts | 
[**delete_pending_contract**](ContractsApi.md#delete_pending_contract) | **DELETE** /api/v1/contracts/{contractId} | 
[**get_compensation_verification_status**](ContractsApi.md#get_compensation_verification_status) | **GET** /api/v1/compensation_verification_status | Verification status of every compensation row of some schools in one season
[**get_contract_history**](ContractsApi.md#get_contract_history) | **GET** /api/v1/contract_history | 
[**list_contract_verifications**](ContractsApi.md#list_contract_verifications) | **GET** /api/v1/contract_verifications | List verification events across contracts
[**publish_pending_contract**](ContractsApi.md#publish_pending_contract) | **POST** /api/v1/contracts/{contractId}/publish | 
[**replace_contract_file**](ContractsApi.md#replace_contract_file) | **PUT** /api/v1/contracts/{contractId}/file | 
[**swap_contract_raw_contracts**](ContractsApi.md#swap_contract_raw_contracts) | **POST** /api/v1/contracts/swap_raw_contracts | 
[**update_contract**](ContractsApi.md#update_contract) | **PATCH** /api/v1/contracts/{contractId} | 


# **create_contract_direct_upload**
> CreateContractDirectUpload200Response create_contract_direct_upload(create_contract_direct_upload_request)

WINAD-10744: step 1 of filing a pending contract PDF over the gateway's 1 MiB body limit. Creates the storage blob and returns the URL and headers to PUT the PDF bytes to, plus `signed_id` to send as `file_signed_id` to POST /contracts. Same payload as Active Storage's direct upload, behind the OAuth token. `winad_write` scope. Only application/pdf is accepted (422 otherwise), and byte_size must be 1 to 26214400 (25 MiB, the same limit as the Drive source). The returned `signed_id` is single-purpose and expires after 2 hours; filing it later is refused with 422 (errors.file_signed_id). When the contract is filed the stored bytes are checked against the declared byte_size and checksum (422, code checksum_mismatch) and then as a PDF (422, code invalid_pdf).


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.create_contract_direct_upload200_response import CreateContractDirectUpload200Response
from winthrop_client_python.models.create_contract_direct_upload_request import CreateContractDirectUploadRequest
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
    create_contract_direct_upload_request = winthrop_client_python.CreateContractDirectUploadRequest() # CreateContractDirectUploadRequest | 

    try:
        api_response = api_instance.create_contract_direct_upload(create_contract_direct_upload_request)
        print("The response of ContractsApi->create_contract_direct_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_contract_direct_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contract_direct_upload_request** | [**CreateContractDirectUploadRequest**](CreateContractDirectUploadRequest.md)|  | 

### Return type

[**CreateContractDirectUpload200Response**](CreateContractDirectUpload200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Blob created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Not a PDF or invalid blob |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pending_contract**
> CreatePendingContract201Response create_pending_contract(coach_id, file_signed_id=file_signed_id, file=file, source_drive_file_id=source_drive_file_id, expected_sha256=expected_sha256, drive_id=drive_id, text=text, contract_terms=contract_terms, change_note=change_note)

File a PDF on a coach as a pending contract. Creates a RawContract with the PDF attached and a Contract with pending true (no dates) in one transaction; nothing is created if the request is refused. Requires the winad_write scope and a manage-level user. The PDF must really be a PDF (its bytes are checked, not its name).

WINAD-10744: a third input, `file_signed_id`, is the signed id of a PDF the client sent straight to storage with POST /contracts/direct_uploads (no gateway body limit); it is read back, checked as a PDF and attached. A blob that is unknown, was never uploaded, is already in use, is not a PDF or fails its checksum is refused with 422 (errors.file_signed_id; code invalid_input or invalid_pdf), and a non-PDF blob is purged.

Send the PDF by EXACTLY ONE of the inputs (WINAD-10673). A request with neither or with both is refused with 422 (errors.file and errors.source_drive_file_id, code invalid_input) before anything is read or downloaded.

1. `file`: a multipart upload of the PDF, as before. Larger bodies than the API gateway's request limit (1 MiB by default) cannot take this route.
2. `source_drive_file_id` plus `expected_sha256`: the server downloads the PDF from Google Drive with its own credentials, so the bytes never pass through the gateway. `source_drive_file_id` is a bare Drive file id (letters, digits, "-" and "_", 10 to 200 characters), never a URL. `expected_sha256` (the 64 hexadecimal characters of the SHA-256 of the reviewed PDF, any case) is required with it and refused with a direct file: if the Drive file's bytes hash differently the request is refused (checksum_mismatch), so changed content never replaces reviewed bytes. The file must be a stored PDF the service account can read (a Google Docs document is refused) and at most 25 MiB; the download must finish within 60 seconds (10 seconds to connect, 30 per read).

`drive_id` keeps its meaning and is independent of `source_drive_file_id`: it is the ORIGINAL source identity, unique per coach (a second request with the same drive_id for the coach is refused with 422 errors.drive_id, whichever Drive file or upload it carries). They may differ, for example when the final composed PDF is a different Drive file from the original. The schema treats a field that is present as sent: leave out the inputs you do not use rather than sending them empty (the server itself tolerates an empty optional field as "not sent"). Only `drive_id` deduplicates: a Drive-source request without drive_id is not deduplicated, exactly like a direct upload without drive_id.

The request stays synchronous. Order of work: authorization, change_note, coach and input checks, then the Drive download, hash and PDF check (no database lock is held meanwhile), then the same transaction, locks, uniqueness and stored-file cleanup as a direct upload. Nothing is created and no file is left behind by any refusal. The response and the pending visibility are the same for both inputs; `filename` is the Drive file's name for a Drive source.

Refusals of the Drive source carry a stable machine-readable `code` next to `errors`: invalid_input (422, a malformed param or the wrong number of inputs), source_unavailable (422, the Drive file does not exist or is not shared with the service account), source_too_large (422), invalid_pdf (422, the bytes are not a PDF or the Drive file is a Google document), checksum_mismatch (422, the message names the hash the Drive file really has), source_timeout and source_error (503 with a Retry-After header: Drive was slow, down or throttling, refused the download, cut the connection before the whole file arrived, or the service credentials failed; the same request may be repeated unchanged, nothing was created).

WINAD-10747: with a JSON body that has `raw_contract_id`, no file is sent. The request files a published Contract (pending false, with dates) for `coach_id` on that existing RawContract and answers 201 with the Contract. Several coaches may each hold a Contract on the same RawContract (a shared staff list), but one coach only once: a second request for the same coach and document is refused with 422 (errors.coach_id). Also refused with 422: an unknown coach or RawContract, a RawContract that is a vendor deal's document, not a COACH document or a pending contract's, a start_on or end_on that is not YYYY-MM-DD or a start after the end, a contractable_type other than Coach, and a school_id that is unknown or is not the school of the document. Nothing is created by a refusal. `change_note` is stored on the audit version as for every write.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.create_pending_contract201_response import CreatePendingContract201Response
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
    file_signed_id = 'file_signed_id_example' # str | Signed id returned by POST /contracts/direct_uploads after the PDF bytes were PUT to the returned URL. Exactly one of file, source_drive_file_id and file_signed_id is required. (optional)
    file = None # bytearray | The contract PDF as a multipart upload. Exactly one of file and source_drive_file_id is required. (optional)
    source_drive_file_id = 'source_drive_file_id_example' # str | Google Drive file id of the PDF to download (not a URL; an id with a slash, a dot or a scheme is refused). Exactly one of file and source_drive_file_id is required, and expected_sha256 goes with it. NOT the deduplication id, see drive_id. (optional)
    expected_sha256 = 'expected_sha256_example' # str | SHA-256 (64 hexadecimal characters, any case) of the PDF that was reviewed. Required with source_drive_file_id, refused with file. The request is refused with checksum_mismatch when the downloaded bytes hash differently. (optional)
    drive_id = 'drive_id_example' # str | Optional original Google Drive id of the source document, the contract's deduplication identity; must be unique for the coach. Independent of source_drive_file_id, which may be a different (final) Drive file. (optional)
    text = 'text_example' # str | Optional Mistral markdown already produced for this PDF, pages separated by a form feed line (\\\"\\\\n\\\\f\\\\n\\\"). When present it is stored as the contract text and no automatic OCR is queued; when absent one automatic OCR job is queued. (optional)
    contract_terms = 'contract_terms_example' # str | Optional structured terms read from the contract, as a JSON-encoded ContractTerms object (see PATCH /raw_contracts/{id}/contract_terms). Stored on the RawContract in the same transaction; an invalid document refuses the upload with errors keyed contract_terms, contract_terms.schema, contract_terms.source.run_id, and so on. Accepted from service (client-credentials) tokens like the rest of the upload; the audit version then records no person. (optional)
    change_note = 'change_note_example' # str | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. (optional)

    try:
        api_response = api_instance.create_pending_contract(coach_id, file_signed_id=file_signed_id, file=file, source_drive_file_id=source_drive_file_id, expected_sha256=expected_sha256, drive_id=drive_id, text=text, contract_terms=contract_terms, change_note=change_note)
        print("The response of ContractsApi->create_pending_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->create_pending_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coach_id** | **int**| The coach the contract is filed on | 
 **file_signed_id** | **str**| Signed id returned by POST /contracts/direct_uploads after the PDF bytes were PUT to the returned URL. Exactly one of file, source_drive_file_id and file_signed_id is required. | [optional] 
 **file** | **bytearray**| The contract PDF as a multipart upload. Exactly one of file and source_drive_file_id is required. | [optional] 
 **source_drive_file_id** | **str**| Google Drive file id of the PDF to download (not a URL; an id with a slash, a dot or a scheme is refused). Exactly one of file and source_drive_file_id is required, and expected_sha256 goes with it. NOT the deduplication id, see drive_id. | [optional] 
 **expected_sha256** | **str**| SHA-256 (64 hexadecimal characters, any case) of the PDF that was reviewed. Required with source_drive_file_id, refused with file. The request is refused with checksum_mismatch when the downloaded bytes hash differently. | [optional] 
 **drive_id** | **str**| Optional original Google Drive id of the source document, the contract&#39;s deduplication identity; must be unique for the coach. Independent of source_drive_file_id, which may be a different (final) Drive file. | [optional] 
 **text** | **str**| Optional Mistral markdown already produced for this PDF, pages separated by a form feed line (\\\&quot;\\\\n\\\\f\\\\n\\\&quot;). When present it is stored as the contract text and no automatic OCR is queued; when absent one automatic OCR job is queued. | [optional] 
 **contract_terms** | **str**| Optional structured terms read from the contract, as a JSON-encoded ContractTerms object (see PATCH /raw_contracts/{id}/contract_terms). Stored on the RawContract in the same transaction; an invalid document refuses the upload with errors keyed contract_terms, contract_terms.schema, contract_terms.source.run_id, and so on. Accepted from service (client-credentials) tokens like the rest of the upload; the audit version then records no person. | [optional] 
 **change_note** | **str**| Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included, and read back through GET /contract_history. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

### Return type

[**CreatePendingContract201Response**](CreatePendingContract201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pending contract was created (multipart upload), or the published contract was created on the existing RawContract (JSON with raw_contract_id) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to create contracts) |  -  |
**422** | The upload was refused (unknown coach, neither or both of file and source_drive_file_id, malformed source_drive_file_id or expected_sha256, non-PDF file, a file name with a NUL character or bytes that are not UTF-8, duplicate drive_id, invalid contract_terms, or a Drive file that is missing, too large, not a PDF or does not match expected_sha256). Drive-source refusals carry a &#x60;code&#x60;. Nothing was created. |  -  |
**503** | The Drive source could not be read right now (code source_timeout or source_error). Retry the same request after the number of seconds in the Retry-After header. Nothing was created. |  * Retry-After - Seconds to wait before repeating the request <br>  |

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

# **get_compensation_verification_status**
> GetCompensationVerificationStatus200Response get_compensation_verification_status(season, school_ids=school_ids, conference_id=conference_id, status=status, q=q, page=page, per_page=per_page)

Verification status of every compensation row of some schools in one season

Computed on request (WINAD-10682), so there is no ETag. One row per compensation row whose school is in
`school_ids` (or is a member of `conference_id`'s primary conference) and whose `year` is `season`, so a season
is the season-ending year, as in `ContractVerification.seasons` (2025-26 is 2026). `status`, first match wins:

* `unlinked`: the row has no contract (the contract and event fields are null).
* `not_verified`: it has a contract but no verification event covers the season.
* `mismatch`, `could_not_verify`, `revoked`: the latest event covering the season has that result.
* `changed_since_verified`: the latest covering event is `passed`, but the row was edited after it
  (`changed_since` says how).
* `verified`: the latest covering event is `passed` and nothing changed since.

The latest covering event is the newest (verified_at DESC, id DESC) event on the row's contract whose `seasons`
include the season: the same rule as `meta.verified_seasons` of GET /raw_contracts/{id}/verifications, so a row
is `verified` or `changed_since_verified` exactly when its season is in that list.

`changed_since` lists, in time order, every change strictly after the event's `verified_at` to: the row's base
salary, talent fee, one-time bonus, relocation or deferred amount (`base_salary_cents`, `talent_fee`,
`one_time_bonus_cents`, `relocation_cents`, `relocation_taxable`, `deferred_comp_cents`); its `year`, `coach_id`, `school_id`, `contract_id` or `contract_status_id`; the row being
created (`row`); a position linked to the row (`position.season_id`, `position.coach_id`,
`position.compensation_id`); the contract moving to another coach (`contract.coach_id`); the PDF being replaced
(`raw_contract.file`) and the school filed on it (`raw_contract.school_id`). A version whose saved data cannot be
read is reported as field `unreadable`. It is empty unless the status is `changed_since_verified`.

The rows that make up the contract's season count too, so a row that was deleted, or unlinked or moved out of
the season after the event, changes every row still in that contract and season, even though those rows were
not touched. They are reconstructed from the history of every row that is or was in the contract: `row` with
`old` `compensation <id>` and `new` null (a row deleted from the season), `row` with `old` null and `new`
`created` (a row created in it, or the same entry for the row itself), `contract_id` with the old and new
contract id (a row linked to or unlinked from the contract, null for none) and `year` with the old and new
season (a row moved into or out of the season). A row that was deleted, unlinked or moved before the event does
not count, nor does a row of another contract or another season of the contract. Not detectable: a position
taken off the row. Each entry names the person who made the change (`user`; null for an edit with no recorded
author), so the endpoint needs the ability to update contracts: a customer gets 403.

`counts_by_status` in `meta` covers the whole scope, before `status[]` and `q`. `status[]` keeps only those
statuses. `q` takes the Ransack filters of GET /contract_verifications (without its school and season scopes)
and applies them to the event in force only, never to older events; a row with no event (`not_verified`,
`unlinked`) is not removed by `q`, so `q[verified_at_lt]=2026-09-15` is "not verified, or verified before
9-15" in one call; add `status[]=verified` to keep only the rows that have an event. A hidden coach's rows are
left out for a caller who cannot manage coaches. Rows are ordered by school, coach, compensation id. The
whole scope is computed on every page; a Big Ten season is a few pages of 500 to 1000.

A 400 is `{ "errors": { "<parameter>": ["..."] } }`, keyed by the parameter that is missing or invalid: `season`,
`school_ids` (also when both or neither of `school_ids` and `conference_id` are given, or more than 300 schools),
`conference_id`, `status`, or `q` (the shared UnknownRansackCondition answer, WINAD-10681: a condition that is
unknown, outside the allowlist or has no predicate). A malformed `page` or `per_page` is a 400 too.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.compensation_verification_status_value import CompensationVerificationStatusValue
from winthrop_client_python.models.get_compensation_verification_status200_response import GetCompensationVerificationStatus200Response
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
    season = 56 # int | Season-ending year, a positive whole number.
    school_ids = [56] # List[int] | The schools to read, as school_ids[]=1&school_ids[]=2 or a comma separated list. At most 300. Give exactly one of school_ids and conference_id. (optional)
    conference_id = 56 # int | The schools whose primary conference this is (not schools that play one sport in it). At most 300 schools; an unknown conference is 400. (optional)
    status = [winthrop_client_python.CompensationVerificationStatusValue()] # List[CompensationVerificationStatusValue] | Keep only rows with these statuses (status[]=verified&status[]=not_verified). (optional)
    q = None # object | Ransack filters on the verification event in force, for example q[verified_at_lt]=2026-09-15T00:00:00Z, q[method_eq]=agent, q[agent_run_id_start]=astra or q[batch_id_eq]=big-ten-2025-a. Same allowlist as GET /contract_verifications, without its bulk-only school scopes; a condition outside it, or one with no predicate, is a 400 naming it (`errors.q`, WINAD-10681). (optional)
    page = 1 # int | results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with `Invalid pagination parameter: page`. (optional) (default to 1)
    per_page = 500 # int | Page size, capped at 1000; defaults to 500. (optional) (default to 500)

    try:
        # Verification status of every compensation row of some schools in one season
        api_response = api_instance.get_compensation_verification_status(season, school_ids=school_ids, conference_id=conference_id, status=status, q=q, page=page, per_page=per_page)
        print("The response of ContractsApi->get_compensation_verification_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->get_compensation_verification_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season-ending year, a positive whole number. | 
 **school_ids** | [**List[int]**](int.md)| The schools to read, as school_ids[]&#x3D;1&amp;school_ids[]&#x3D;2 or a comma separated list. At most 300. Give exactly one of school_ids and conference_id. | [optional] 
 **conference_id** | **int**| The schools whose primary conference this is (not schools that play one sport in it). At most 300 schools; an unknown conference is 400. | [optional] 
 **status** | [**List[CompensationVerificationStatusValue]**](CompensationVerificationStatusValue.md)| Keep only rows with these statuses (status[]&#x3D;verified&amp;status[]&#x3D;not_verified). | [optional] 
 **q** | [**object**](.md)| Ransack filters on the verification event in force, for example q[verified_at_lt]&#x3D;2026-09-15T00:00:00Z, q[method_eq]&#x3D;agent, q[agent_run_id_start]&#x3D;astra or q[batch_id_eq]&#x3D;big-ten-2025-a. Same allowlist as GET /contract_verifications, without its bulk-only school scopes; a condition outside it, or one with no predicate, is a 400 naming it (&#x60;errors.q&#x60;, WINAD-10681). | [optional] 
 **page** | **int**| results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with &#x60;Invalid pagination parameter: page&#x60;. | [optional] [default to 1]
 **per_page** | **int**| Page size, capped at 1000; defaults to 500. | [optional] [default to 500]

### Return type

[**GetCompensationVerificationStatus200Response**](GetCompensationVerificationStatus200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page of rows |  -  |
**400** | A &#x60;q[...]&#x60; condition names an attribute, association path, predicate or scope the resource does not expose, or names an attribute without a predicate (&#x60;q[name]&#x3D;x&#x60; instead of &#x60;q[name_eq]&#x3D;x&#x60; or &#x60;q[name_cont]&#x3D;x&#x60;, and a &#x60;q[c]&#x60; list entry without &#x60;p&#x60;). The search is refused instead of silently ignoring the condition, which would return the unfiltered collection. &#x60;errors.q&#x60; has one entry per bad condition: &#x60;unknown condition: &lt;name&gt;&#x60;, or &#x60;condition has no predicate: &lt;name&gt; (use &lt;name&gt;_eq, &lt;name&gt;_cont, ...)&#x60;. Sorting (&#x60;q[s]&#x60;), the combinator (&#x60;q[m]&#x60;), groups (&#x60;q[g]&#x60;) and a condition whose value is blank are not refused. A 400 on these operations can also be an invalid pagination parameter, or a &#x60;q&#x60; of the wrong shape (&#x60;Unexpected format for q param: ...&#x60;: &#x60;q&#x60; must be a hash, a JSON object string, or absent, and &#x60;q[c]&#x60; and &#x60;q[g]&#x60; a hash or a list of hashes, so &#x60;q[]&#x3D;x&#x60; and &#x60;q[c]&#x3D;x&#x60; are refused instead of returning the unfiltered collection); for these &#x60;errors&#x60; is a list of messages. |  -  |
**401** | Unauthorized |  -  |
**403** | Missing winad_read scope, or not permitted to update contracts (staff only) |  -  |

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

# **list_contract_verifications**
> ListContractVerifications200Response list_contract_verifications(page=page, per_page=per_page, q=q)

List verification events across contracts

The verification history of many contracts in one request (WINAD-10680), instead of one
GET /raw_contracts/{id}/verifications per document. Read-only. Each row is exactly what the per-contract read
returns for the same event (the ContractVerification schema); that endpoint is unchanged. There is no
`verified_seasons` in the meta, since that is a per-contract summary; derive it from the events, newest first
(a season counts as verified when its latest event is `passed`).

Ordering is always verified_at DESC, id DESC, so pages never overlap or skip. Ransack filters, with the same
allowlist as the per-contract read (id, contract_id, raw_contract_id, coach_id, verified_by_id, verified_at,
result, method, agent_run_id, evidence_url, created_at, batch_id, code_version; association traversal and
predicates on `seasons` are not available; a filter outside the allowlist, or an attribute without a predicate,
is a 400 naming it, WINAD-10681). Examples: everything verified on 2026-10-10 is
`q[verified_at_gteq]=2026-10-10&q[verified_at_lt]=2026-10-11`, one posting batch is `q[batch_id_eq]=...`, runs
of one bot are `q[agent_run_id_start]=...`. Three filters exist only here:
`q[contract_school_id_eq]` and `q[contract_school_id_in][]` keep the events of contracts whose coach has (or
had) a position at that school, as the contracts index's `contract_school_id_eq` does, and
`q[seasons_contains]=2025` keeps the events whose `seasons` include that year (one whole number, within the
32-bit range; anything else is 400 `errors.q.seasons_contains`). A list filter takes at
most 1000 values (more is 422 `errors.q.<filter>`; a comma separated string counts the same). Ids go in the
query string, so for a larger set page through `contract_school_id_in` or a smaller `contract_id_in` slice.
For a season-by-season status per compensation row use GET /compensation_verification_status.

Visibility is the per-contract read's, applied to every contract in one query: only events of contracts whose
RawContract the caller may read, and that the contracts API serves them, are returned (a hidden coach's contracts
and pending contracts are left out for anyone who cannot manage coaches, with the counts to match). A
contract with no document is not listed. A caller who may not read documents at all gets 403.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.list_contract_verifications200_response import ListContractVerifications200Response
from winthrop_client_python.models.list_contract_verifications_q_parameter import ListContractVerificationsQParameter
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
    page = 1 # int | results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with `Invalid pagination parameter: page`. (optional) (default to 1)
    per_page = 100 # int | Page size, capped at 500; defaults to 100. (optional) (default to 100)
    q = winthrop_client_python.ListContractVerificationsQParameter() # ListContractVerificationsQParameter | Ransack filters, for example q[contract_id_in][]=1&q[contract_id_in][]=2, q[contract_school_id_eq]=7, q[result_eq]=passed, q[seasons_contains]=2025, q[batch_id_eq]=big-ten-2025-a, q[code_version_start]=0c2950e or q[s]=verified_at asc. At most 1000 values in any list. (optional)

    try:
        # List verification events across contracts
        api_response = api_instance.list_contract_verifications(page=page, per_page=per_page, q=q)
        print("The response of ContractsApi->list_contract_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->list_contract_verifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with &#x60;Invalid pagination parameter: page&#x60;. | [optional] [default to 1]
 **per_page** | **int**| Page size, capped at 500; defaults to 100. | [optional] [default to 100]
 **q** | [**ListContractVerificationsQParameter**](.md)| Ransack filters, for example q[contract_id_in][]&#x3D;1&amp;q[contract_id_in][]&#x3D;2, q[contract_school_id_eq]&#x3D;7, q[result_eq]&#x3D;passed, q[seasons_contains]&#x3D;2025, q[batch_id_eq]&#x3D;big-ten-2025-a, q[code_version_start]&#x3D;0c2950e or q[s]&#x3D;verified_at asc. At most 1000 values in any list. | [optional] 

### Return type

[**ListContractVerifications200Response**](ListContractVerifications200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One page of events |  -  |
**304** | Nothing in the page has changed (ETag) |  -  |
**400** | A &#x60;q[...]&#x60; condition names an attribute, association path, predicate or scope the resource does not expose, or names an attribute without a predicate (&#x60;q[name]&#x3D;x&#x60; instead of &#x60;q[name_eq]&#x3D;x&#x60; or &#x60;q[name_cont]&#x3D;x&#x60;, and a &#x60;q[c]&#x60; list entry without &#x60;p&#x60;). The search is refused instead of silently ignoring the condition, which would return the unfiltered collection. &#x60;errors.q&#x60; has one entry per bad condition: &#x60;unknown condition: &lt;name&gt;&#x60;, or &#x60;condition has no predicate: &lt;name&gt; (use &lt;name&gt;_eq, &lt;name&gt;_cont, ...)&#x60;. Sorting (&#x60;q[s]&#x60;), the combinator (&#x60;q[m]&#x60;), groups (&#x60;q[g]&#x60;) and a condition whose value is blank are not refused. A 400 on these operations can also be an invalid pagination parameter, or a &#x60;q&#x60; of the wrong shape (&#x60;Unexpected format for q param: ...&#x60;: &#x60;q&#x60; must be a hash, a JSON object string, or absent, and &#x60;q[c]&#x60; and &#x60;q[g]&#x60; a hash or a list of hashes, so &#x60;q[]&#x3D;x&#x60; and &#x60;q[c]&#x3D;x&#x60; are refused instead of returning the unfiltered collection); for these &#x60;errors&#x60; is a list of messages. |  -  |
**401** | Unauthorized |  -  |
**403** | Missing winad_read scope, or not permitted to read documents |  -  |
**422** | A list filter has more than 1000 values (errors.q.&lt;filter&gt;) |  -  |

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
**422** | Missing or non-PDF file, a file name with a NUL character or bytes that are not UTF-8 (errors.file), a contract with no PDF record, a PDF another record uses, or an invalid change_note (errors.change_note). The old file is untouched. |  -  |
**409** | The contract was moved to another coach again and again while the request waited for its locks (errors.contract). Nothing was written; reload the contract and retry. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swap_contract_raw_contracts**
> SwapContractRawContracts200Response swap_contract_raw_contracts(swap_contract_raw_contracts_request)

Exchange the RawContracts (PDFs) of two published coach contracts in one transaction (WINAD-10727), for documents filed crossed: each contract's pay rows are right and each holds the other's PDF. Afterwards each contract holds the other's former RawContract. Same refusals as PATCH /contracts/{contractId} raw_contract_id: 422 (errors keyed by contract_ids or contract_<id>) when contract_ids is not two different positive integers, a contract is pending, or a document is a vendor deal's or not a COACH contract document; any refusal leaves both contracts unchanged. WINAD-10745: expected_raw_contract_ids is required, an object keyed by the two contract ids with the RawContract id each holds now; it is checked under the locks, and if either contract holds another RawContract the response is 422 (errors keyed contract_<id>, naming what it holds now) and nothing is written. A missing or malformed expected_raw_contract_ids is a 422 keyed expected_raw_contract_ids. Verification events and pay rows are not touched. The optional top-level change_note is stored on both contracts' versions. Requires winad_write and a manage-level user with a user-backed OAuth token.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.swap_contract_raw_contracts200_response import SwapContractRawContracts200Response
from winthrop_client_python.models.swap_contract_raw_contracts_request import SwapContractRawContractsRequest
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
    swap_contract_raw_contracts_request = winthrop_client_python.SwapContractRawContractsRequest() # SwapContractRawContractsRequest | 

    try:
        api_response = api_instance.swap_contract_raw_contracts(swap_contract_raw_contracts_request)
        print("The response of ContractsApi->swap_contract_raw_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContractsApi->swap_contract_raw_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swap_contract_raw_contracts_request** | [**SwapContractRawContractsRequest**](SwapContractRawContractsRequest.md)|  | 

### Return type

[**SwapContractRawContracts200Response**](SwapContractRawContracts200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contracts and the RawContract each holds now |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope, not a manage-level user, or a token with no user) |  -  |
**404** | A contract was not found |  -  |
**409** | A contract was moved to another coach again and again while the request waited for its locks. Nothing was written. |  -  |
**422** | Refused (see the description). Nothing was written. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contract**
> Contract update_contract(contract_id, update_contract_request)

Edit a published contract's start_on, end_on, executed_on, expires_on, at_will, contingent_change, coach_id and raw_contract_id (WINAD-10631, WINAD-10639, WINAD-10727). Only supplied fields change; linked compensations are unchanged. Pending contracts are published, not edited (use POST /contracts/{contractId}/publish); the only fields a pending contract accepts are the owner fields coach_id, contractable_id and contractable_type (WINAD-10739), so a contract saved without a contractable_type can be repaired before it is published.
Dates must be YYYY-MM-DD and flags JSON true or false (the same rules as publish). Setting at_will true requires end_on null; send both fields to clear a stored end date. The at-will/end-date rule is checked only when either field is supplied, allowing start-only corrections on legacy rows. end_on, executed_on and expires_on can be cleared with null.
coach_id moves the contract to another coach, in the same transaction as the other fields. A move is refused with 422 (errors.coach_id) when the coach does not exist or is not visible to the caller, or while any compensation, any position of those compensations, any verification event still in force (the newest event of a season is not a revocation; a contract whose seasons are all revoked can move and keeps its events unchanged) or any earned incentive still links to the contract (an earned incentive links through its raw_contract_id or its ended_by_contract_id being the contract's RawContract): the body then also lists linked_compensation_ids, linked_position_ids, linked_verification_ids and linked_earned_incentive_ids, and nothing is written. Never move those rows from the API; a person unlinks or moves them first. Sending the coach it already has is a no-op.
A move also files the contract's PDF under the new coach's current school (raw_contracts.school_id, the school the pending upload sets, null when the new coach has no current position), in the same transaction. A PDF that another record also uses (another contract, a game contract, a deal and so on) or a financial report is left unchanged, and so is the school when the move is refused or the coach is unchanged. The school change is a RawContract entry in GET /contract_history, under the new coach, with the change_note and the user, and the response body is unchanged.
raw_contract_id changes which RawContract (PDF) the contract holds (WINAD-10727), for a document filed on the wrong contract; linked pay rows and verification events are not touched (events stay recorded against the coach and RawContract they were made for). It is refused with 422 (errors.raw_contract_id) when the RawContract does not exist, is a vendor deal's document (deal_id set), is not of the COACH contract type, or is already held by another contract (the message names it; use POST /contracts/swap_raw_contracts to exchange two). It is also refused when the document it replaces belongs to a hidden coach and no other record would hold it afterwards (it would become readable by customers). The contract itself must not be pending. Sending the RawContract it already holds is a no-op.
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

