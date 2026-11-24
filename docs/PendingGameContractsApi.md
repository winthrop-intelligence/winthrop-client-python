# winthrop_client_python.PendingGameContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pending_game_contract**](PendingGameContractsApi.md#create_pending_game_contract) | **POST** /api/v1/pending_game_contracts | 
[**delete_pending_game_contract**](PendingGameContractsApi.md#delete_pending_game_contract) | **DELETE** /api/v1/pending_game_contracts/{raw_contractId} | 
[**get_pending_game_contracts**](PendingGameContractsApi.md#get_pending_game_contracts) | **GET** /api/v1/pending_game_contracts | 
[**publish_pending_game_contract**](PendingGameContractsApi.md#publish_pending_game_contract) | **POST** /api/v1/pending_game_contracts/{raw_contractId}/publish | 


# **create_pending_game_contract**
> PendingGameContract create_pending_game_contract(school_id, foia_label_id=foia_label_id, drive_id=drive_id, text=text, file=file, source_drive_file_id=source_drive_file_id, expected_sha256=expected_sha256, file_signed_id=file_signed_id)

File a guarantee PDF as a pending GAME RawContract (WINAD-10815), the game counterpart of POST /contracts (coach) and POST /deals (vendor). The PDF comes from exactly one of `file` (multipart), `source_drive_file_id` with `expected_sha256` (a Google Drive file, downloaded and verified by WinAD) or `file_signed_id` (a blob sent straight to storage with POST /contracts/direct_uploads), with the same PDF checks and refusal codes as POST /contracts. `school_id` is the school whose FOIA request produced the PDF. Optional `foia_label_id` (kept for the list filter), `drive_id` (the source Drive file) and `text` (the splitter's Mistral text, pages separated by a form feed; without it the one OCR job is queued).

The RawContract is pending and internal-only (the same rule as a pending coach contract's PDF: only super admins and service tokens can read its record, file or text) and has no GameContracts. A second PDF of the same school with the same `drive_id` or the same SHA-256 is refused with 422 (`errors.drive_id` / `errors.file`, code `duplicate`) and nothing is stored. Requires winad_write and a manage-level user.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.pending_game_contract import PendingGameContract
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
    api_instance = winthrop_client_python.PendingGameContractsApi(api_client)
    school_id = 56 # int | 
    foia_label_id = 56 # int |  (optional)
    drive_id = 'drive_id_example' # str | The original source Drive file id, the per-school duplicate key. (optional)
    text = 'text_example' # str | Mistral OCR markdown of the PDF; stored as the RawContract text so no second OCR runs. (optional)
    file = None # bytearray |  (optional)
    source_drive_file_id = 'source_drive_file_id_example' # str |  (optional)
    expected_sha256 = 'expected_sha256_example' # str | SHA-256 of the Drive file; only with source_drive_file_id. (optional)
    file_signed_id = 'file_signed_id_example' # str | Signed id from POST /contracts/direct_uploads. (optional)

    try:
        api_response = api_instance.create_pending_game_contract(school_id, foia_label_id=foia_label_id, drive_id=drive_id, text=text, file=file, source_drive_file_id=source_drive_file_id, expected_sha256=expected_sha256, file_signed_id=file_signed_id)
        print("The response of PendingGameContractsApi->create_pending_game_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PendingGameContractsApi->create_pending_game_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **int**|  | 
 **foia_label_id** | **int**|  | [optional] 
 **drive_id** | **str**| The original source Drive file id, the per-school duplicate key. | [optional] 
 **text** | **str**| Mistral OCR markdown of the PDF; stored as the RawContract text so no second OCR runs. | [optional] 
 **file** | **bytearray**|  | [optional] 
 **source_drive_file_id** | **str**|  | [optional] 
 **expected_sha256** | **str**| SHA-256 of the Drive file; only with source_drive_file_id. | [optional] 
 **file_signed_id** | **str**| Signed id from POST /contracts/direct_uploads. | [optional] 

### Return type

[**PendingGameContract**](PendingGameContract.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pending guarantee PDF was filed. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not a manage-level user) |  -  |
**422** | Unknown school or label, an invalid input combination or PDF, a checksum mismatch, or a duplicate. Nothing was stored. |  -  |
**503** | Google Drive was temporarily unavailable (&#x60;source_timeout&#x60;, &#x60;source_error&#x60;); retry unchanged after Retry-After. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pending_game_contract**
> delete_pending_game_contract(raw_contract_id, expected_sha256)

Delete a pending guarantee PDF (cruft or a duplicate) and its stored file (WINAD-10815). The request carries `expected_sha256` (query or body), the digest of the PDF the caller reviewed. Inside the deletion transaction WinAD rechecks that the document is a GAME RawContract, still pending and that its stored PDF has that digest, and refuses on any mismatch, so a replacement PDF filed under the id and a PDF published a moment ago both survive. A document with GameContracts or used by another record is never deleted. Requires winad_write and a manage-level user.


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
    api_instance = winthrop_client_python.PendingGameContractsApi(api_client)
    raw_contract_id = 56 # int | 
    expected_sha256 = 'expected_sha256_example' # str | 

    try:
        api_instance.delete_pending_game_contract(raw_contract_id, expected_sha256)
    except Exception as e:
        print("Exception when calling PendingGameContractsApi->delete_pending_game_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_contract_id** | **int**|  | 
 **expected_sha256** | **str**|  | 

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
**204** | Deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**422** | Not a pending GAME PDF, a malformed digest (&#x60;errors.expected_sha256&#x60;), a digest that does not match the stored PDF (code &#x60;checksum_mismatch&#x60;) or a PDF another record uses. Nothing was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_game_contracts**
> PendingGameContractCollection get_pending_game_contracts(school_id=school_id, foia_label_id=foia_label_id, page=page, per_page=per_page)

List the pending guarantee (GAME) PDFs, across schools (WINAD-10815), oldest first, filterable by school and FOIA label. Each row has the RawContract id, school, filename, created_at, the SHA-256 of the stored PDF and whether its OCR text is ready (`ocr_text_ready`); read the text itself with GET /raw_contracts/{raw_contractId}/ocr_text. A PDF published with every occurrence skipped is not listed. Requires winad_read and a manage-level user (client-credentials service tokens included).


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.pending_game_contract_collection import PendingGameContractCollection
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
    api_instance = winthrop_client_python.PendingGameContractsApi(api_client)
    school_id = 56 # int |  (optional)
    foia_label_id = 56 # int |  (optional)
    page = 1 # int | results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with `Invalid pagination parameter: page`. (optional) (default to 1)
    per_page = 20 # int | number of results per page. At most 2147483647 (a larger value is a 400 with `Invalid pagination parameter: per_page`); most endpoints also cap it at 100. (optional) (default to 20)

    try:
        api_response = api_instance.get_pending_game_contracts(school_id=school_id, foia_label_id=foia_label_id, page=page, per_page=per_page)
        print("The response of PendingGameContractsApi->get_pending_game_contracts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PendingGameContractsApi->get_pending_game_contracts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **int**|  | [optional] 
 **foia_label_id** | **int**|  | [optional] 
 **page** | **int**| results page to retrieve. At most 2147483647 (a signed 32-bit integer); a larger value, like 0 or a non-number, is a 400 with &#x60;Invalid pagination parameter: page&#x60;. | [optional] [default to 1]
 **per_page** | **int**| number of results per page. At most 2147483647 (a larger value is a 400 with &#x60;Invalid pagination parameter: per_page&#x60;); most endpoints also cap it at 100. | [optional] [default to 20]

### Return type

[**PendingGameContractCollection**](PendingGameContractCollection.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The pending guarantee PDFs. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_read scope or not a manage-level user) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_pending_game_contract**
> PendingGameContractReceipt publish_pending_game_contract(raw_contract_id, publish_pending_game_contract_request)

Publish a pending guarantee PDF (WINAD-10815) in ONE transaction: one GameContract per written occurrence, each linked to its existing Game(s), and pending cleared. It uses the RawContract that already exists (no second upload). The body is the per-occurrence plan of POST /game_contracts/apply (`game_ids`, `expected_games`, `game_contract`, with `occurrence_id` for `action_id`) plus the source binding `raw_contract_id` (must equal the path id) and `expected_sha256` (the stored PDF's digest). The Game snapshot also carries `neutral`, rechecked in the transaction. `game_contract.verified` is optional and may only be false: published rows stay unverified.

`occurrences` lists every reviewed occurrence of the PDF, non-empty with unique `occurrence_id`s, each exactly one disposition: a write (`game_ids`, `expected_games`, `game_contract`) or `skip` with a `reason`. The client guarantees the list is complete against the PDF; the server cannot know the true count. A write needs an existing Game (creating one while publishing awaits WINAD-10376: until then a write with a missing Game is refused with 409 and the PDF stays pending); a skip needs none. A PDF where every occurrence is skipped is valid: it creates no rows, is marked processed and stays internal-only to customers. A PDF with at least one write becomes customer-visible through its GameContracts. Linking a Game keeps the standard side effects, including marking its FOIA requested items received.

Under the RawContract's row lock WinAD rechecks that it is still a pending GAME PDF with the stored digest, and under the Games' locks that each still matches its snapshot (`neutral` included) and has no GameContract. Any refusal writes nothing and leaves the PDF pending. The receipt (RawContract id and, per occurrence, the occurrence id with the Game and GameContract ids, or the approved skip reason) is stored in the same transaction: an identical retry returns the original receipt (`status: already_published`) and writes nothing; a different request for a published PDF is refused. Requires winad_write and a manage-level user.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.pending_game_contract_receipt import PendingGameContractReceipt
from winthrop_client_python.models.publish_pending_game_contract_request import PublishPendingGameContractRequest
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
    api_instance = winthrop_client_python.PendingGameContractsApi(api_client)
    raw_contract_id = 56 # int | 
    publish_pending_game_contract_request = winthrop_client_python.PublishPendingGameContractRequest() # PublishPendingGameContractRequest | 

    try:
        api_response = api_instance.publish_pending_game_contract(raw_contract_id, publish_pending_game_contract_request)
        print("The response of PendingGameContractsApi->publish_pending_game_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PendingGameContractsApi->publish_pending_game_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_contract_id** | **int**|  | 
 **publish_pending_game_contract_request** | [**PublishPendingGameContractRequest**](PublishPendingGameContractRequest.md)|  | 

### Return type

[**PendingGameContractReceipt**](PendingGameContractReceipt.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Published, or an identical retry of a publish that already succeeded. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | A Game changed after review (including &#x60;neutral&#x60;), already has a GameContract or does not exist. Nothing was written. |  -  |
**422** | Invalid body, a PDF that is not pending or whose digest changed, or a GameContract the model refuses. Nothing was written and the PDF is still pending. |  -  |
**503** | The automation actor used for the audit trail is unavailable. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

