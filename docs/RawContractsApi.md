# winthrop_client_python.RawContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_raw_contract_contract_terms**](RawContractsApi.md#get_raw_contract_contract_terms) | **GET** /api/v1/raw_contracts/{raw_contractId}/contract_terms | 
[**regenerate_raw_contract_ocr_text**](RawContractsApi.md#regenerate_raw_contract_ocr_text) | **POST** /api/v1/raw_contracts/{raw_contractId}/ocr_text/regenerate | 
[**replace_raw_contract_file**](RawContractsApi.md#replace_raw_contract_file) | **PUT** /api/v1/raw_contracts/{raw_contractId}/file | 
[**update_raw_contract_contract_terms**](RawContractsApi.md#update_raw_contract_contract_terms) | **PATCH** /api/v1/raw_contracts/{raw_contractId}/contract_terms | 


# **get_raw_contract_contract_terms**
> RawContractTerms get_raw_contract_contract_terms(raw_contract_id)

Return the structured contract terms stored on a RawContract (WINAD-10633), and whether the contract's OCR text has changed since they were read (contract_terms_stale).

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.raw_contract_terms import RawContractTerms
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
    api_instance = winthrop_client_python.RawContractsApi(api_client)
    raw_contract_id = 56 # int | ID of the RawContract

    try:
        api_response = api_instance.get_raw_contract_contract_terms(raw_contract_id)
        print("The response of RawContractsApi->get_raw_contract_contract_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawContractsApi->get_raw_contract_contract_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_contract_id** | **int**| ID of the RawContract | 

### Return type

[**RawContractTerms**](RawContractTerms.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored terms (contract_terms is null when none have been stored) |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (insufficient scope, or a document the user cannot read) |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_raw_contract_ocr_text**
> RegenerateRawContractOcrText200Response regenerate_raw_contract_ocr_text(raw_contract_id)

Re-run Mistral OCR on a raw contract's PDF (WINAD-10683). Queues RawContractOcrJob, which replaces the stored
OCR `text` with page-separated Mistral text (pages joined by "\n\f\n"); the contract's text state reads
`processing` until the job finishes. Poll GET /raw_contracts/{raw_contractId}/ocr_text for the result. Use it to
refresh text stored before the page separator existed. Admin (manage) users only; a token with any scope is
accepted, and the endpoint does not take `change_note`. `POST /raw_contracts/{raw_contractId}/unstract_pdf_text`
is the deprecated alias of this endpoint.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.regenerate_raw_contract_ocr_text200_response import RegenerateRawContractOcrText200Response
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
    api_instance = winthrop_client_python.RawContractsApi(api_client)
    raw_contract_id = 56 # int | ID of the RawContract

    try:
        api_response = api_instance.regenerate_raw_contract_ocr_text(raw_contract_id)
        print("The response of RawContractsApi->regenerate_raw_contract_ocr_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawContractsApi->regenerate_raw_contract_ocr_text: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_contract_id** | **int**| ID of the RawContract | 

### Return type

[**RegenerateRawContractOcrText200Response**](RegenerateRawContractOcrText200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Text extraction queued |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (the user may not manage raw contracts) |  -  |
**404** | Not Found |  -  |
**422** | No file attached to the raw contract |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_raw_contract_file**
> RawContract replace_raw_contract_file(raw_contract_id, file, change_note=change_note)

Replace the PDF of a vendor deal's RawContract (WINAD-10684). Send multipart/form-data with the new PDF as `file` and an optional `change_note`. The RawContract keeps its id and its `deal_id` link. The old file (and its OCR copy) is replaced, not kept as an attachment; the stored text is cleared and Mistral OCR is queued once, the way the admin's Re-extract does, so `text` (and GET /raw_contracts/{id}/ocr_text) reflect the new file once the extraction finishes. The structured `contract_terms` are not touched (they read as stale against the new text). `asset_file_name`, `asset_file_size` and `asset_content_type` are set from the new file and `updated_at` moves, so the response shows the new file name, size and time.

Vendor RawContracts only: a RawContract with no deal, one that belongs to a coach contract (use PUT /contracts/{contractId}/file) or one that a game contract, income report, termination agreement, subscription or system setting also uses is refused with 422 (errors.base) and nothing changes. The file must really be a PDF (its bytes are checked, not its name).

The replacement is recorded as exactly one PaperTrail version of the RawContract (no empty touch versions) with a `file` change (filename, byte_size, checksum and content_type, old and new) together with the legacy file columns, the acting user, the API client and the change_note. It is not linked to a contract, so GET /contract_history does not list it. Requires winad_write and a user-backed OAuth token (client-credentials tokens are refused) with permission to update the RawContract.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.raw_contract import RawContract
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
    api_instance = winthrop_client_python.RawContractsApi(api_client)
    raw_contract_id = 56 # int | ID of the vendor deal's RawContract whose PDF is replaced
    file = None # bytearray | The new contract PDF
    change_note = 'change_note_example' # str | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates. At most 500 characters after trimming; blank is the same as omitted; a value that is not text or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. (optional)

    try:
        api_response = api_instance.replace_raw_contract_file(raw_contract_id, file, change_note=change_note)
        print("The response of RawContractsApi->replace_raw_contract_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawContractsApi->replace_raw_contract_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_contract_id** | **int**| ID of the vendor deal&#39;s RawContract whose PDF is replaced | 
 **file** | **bytearray**| The new contract PDF | 
 **change_note** | **str**| Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates. At most 500 characters after trimming; blank is the same as omitted; a value that is not text or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

### Return type

[**RawContract**](RawContract.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The file was replaced and OCR queued. The RawContract is returned as by GET /raw_contracts/{raw_contractId}. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope, a client-credentials token with no user, or not permitted to update the RawContract) |  -  |
**404** | Not Found (no such RawContract, or a coach contract&#39;s document the caller may not see, or the RawContract was deleted while the request ran). The body is a short &#x60;error&#x60; message naming the model and id; it never repeats the caller&#39;s visibility rule. |  -  |
**422** | Missing or non-PDF file, a file name longer than 255 characters (counted after Active Storage&#39;s sanitiser; the legacy &#x60;asset_file_name&#x60; column holds 255) or with a NUL character or bytes that are not UTF-8 (all errors.file), a RawContract that is not a vendor deal&#39;s (errors.base), or an invalid change_note (errors.change_note). The old file is untouched and nothing is stored. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_raw_contract_contract_terms**
> RawContractTerms update_raw_contract_contract_terms(raw_contract_id, contract_terms, change_note=change_note)

Replace the whole contract_terms document on a RawContract (WINAD-10633). The body is the document itself: a JSON object with a `schema` string (for example "ticketing-terms-v1" or "coach-terms-v1") and a `source` object (`rendition_sha256`, `run_id`, `extracted_at`, `method`). Every other key is a term and is stored as sent; terms are not validated beyond the envelope. `source.rendition_sha256` is the SHA-256 (hex) of the OCR text the terms were read from (the `text` returned by GET /raw_contracts/{id}/ocr_text); when that text later changes, `contract_terms_stale` is true.

Every change is recorded in the audit trail (who, old and new value, when, and the optional change_note query parameter as the reason), so this requires the winad_write scope and a user-backed token (client-credentials tokens are refused) with permission to update the RawContract.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.contract_terms import ContractTerms
from winthrop_client_python.models.raw_contract_terms import RawContractTerms
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
    api_instance = winthrop_client_python.RawContractsApi(api_client)
    raw_contract_id = 56 # int | ID of the RawContract
    contract_terms = winthrop_client_python.ContractTerms() # ContractTerms | 
    change_note = 'change_note_example' # str | Optional. Why the terms are being written, for the internal audit history; stored on the audit version this write creates (GET /contract_history does not list RawContract versions, so it is not shown there). It is a query parameter because the request body is the terms document: a `change_note` key in the body is stored as a term and never used as the note. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (change_note[]=a, change_note[k]=v, or containing a NUL character) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned. (optional)

    try:
        api_response = api_instance.update_raw_contract_contract_terms(raw_contract_id, contract_terms, change_note=change_note)
        print("The response of RawContractsApi->update_raw_contract_contract_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawContractsApi->update_raw_contract_contract_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_contract_id** | **int**| ID of the RawContract | 
 **contract_terms** | [**ContractTerms**](ContractTerms.md)|  | 
 **change_note** | **str**| Optional. Why the terms are being written, for the internal audit history; stored on the audit version this write creates (GET /contract_history does not list RawContract versions, so it is not shown there). It is a query parameter because the request body is the terms document: a &#x60;change_note&#x60; key in the body is stored as a term and never used as the note. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (change_note[]&#x3D;a, change_note[k]&#x3D;v, or containing a NUL character) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned. | [optional] 

### Return type

[**RawContractTerms**](RawContractTerms.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The terms were stored |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope, client-credentials token, or not permitted to update the RawContract) |  -  |
**404** | Not Found |  -  |
**422** | The body is not a JSON object, &#x60;schema&#x60; or &#x60;source&#x60; is missing or invalid, or the change_note query parameter is not text or is longer than 500 characters (errors.change_note). Nothing was changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

