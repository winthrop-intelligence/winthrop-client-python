# winthrop_client_python.RawContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_raw_contract**](RawContractsApi.md#create_raw_contract) | **POST** /api/v1/raw_contracts | 
[**get_raw_contract_contract_terms**](RawContractsApi.md#get_raw_contract_contract_terms) | **GET** /api/v1/raw_contracts/{raw_contractId}/contract_terms | 
[**regenerate_raw_contract_ocr_text**](RawContractsApi.md#regenerate_raw_contract_ocr_text) | **POST** /api/v1/raw_contracts/{raw_contractId}/ocr_text/regenerate | 
[**replace_raw_contract_file**](RawContractsApi.md#replace_raw_contract_file) | **PUT** /api/v1/raw_contracts/{raw_contractId}/file | 
[**update_raw_contract_contract_terms**](RawContractsApi.md#update_raw_contract_contract_terms) | **PATCH** /api/v1/raw_contracts/{raw_contractId}/contract_terms | 


# **create_raw_contract**
> RawContractUploaded create_raw_contract(file, coach_id, school_id=school_id, start_on=start_on, end_on=end_on, change_note=change_note)

File a PDF as a coach's RawContract (WINAD-10702), for example an outside-income form a school emailed, so that it can be attached to the coach's income report: take the returned `id` and send it as `raw_contract_id` to PATCH /income_reports/{incomeReportId} (or POST /income_reports). Send multipart/form-data with the PDF as `file` and the owner as `coach_id`. The file must really be a PDF (its bytes are checked, not its name or declared type) and its name at most 255 characters (counted after Active Storage's sanitiser, as for PUT /raw_contracts/{raw_contractId}/file). There is no size limit of our own: the API gateway's request limit applies.

This creates a RawContract only, not a pending contract: unlike POST /contracts it adds nothing to the contract-entry queue and no Contract exists for the document. A RawContract has no coach column; the income report that takes the document over carries the coach. `coach_id` must be a coach the caller may see and decides the document's school: the coach's current school (null without a position this season), or `school_id` when it is sent. The document is a COACH one, so exactly one Mistral OCR job is queued, as for an upload in the admin UI; read the text from GET /raw_contracts/{raw_contractId}/ocr_text once it finishes. The file is served by GET /raw_contracts/{raw_contractId}/view_file and /download.

`start_on` and `end_on` are the dates of a Contract, which a RawContract cannot hold. Send both (YYYY-MM-DD, the end not before the start) to file a dated, published Coach contract on the coach in the same transaction, as the admin's contract upload does (`contract_id` is then set); send neither to create no Contract. One of them alone is refused. Use POST /contracts and its publish call for an undated pending contract or an at-will one.

Until the document is attached, a document sent without dates has no owner record, so the hidden-coach protection (which follows a Contract, income report or termination agreement) does not yet apply to it, even for a coach with visible=false: it is readable like any other RawContract by every caller who may read RawContracts. Attach it to the income report promptly; once attached, or when `start_on` and `end_on` are sent, it is withheld from callers who cannot see the coach.

Everything is created in one transaction after the checks pass, and the stored file is removed again if it fails: a refusal leaves no blob, RawContract or Contract. The creation is recorded in the RawContract's audit history with the acting user (none for a client-credentials token), the API client and the optional change_note. Requires the winad_write scope and a user who may create RawContracts.


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.raw_contract_uploaded import RawContractUploaded
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
    file = None # bytearray | The PDF
    coach_id = 56 # int | The coach the document is filed for
    school_id = 56 # int | Optional. The school the document is filed under. Defaults to the coach's current school. (optional)
    start_on = '2013-10-20' # date | Optional, YYYY-MM-DD. Together with end_on it also files a dated Coach contract (see above). (optional)
    end_on = '2013-10-20' # date | Optional, YYYY-MM-DD, not before start_on. Required with start_on and refused without it. (optional)
    change_note = 'change_note_example' # str | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. (optional)

    try:
        api_response = api_instance.create_raw_contract(file, coach_id, school_id=school_id, start_on=start_on, end_on=end_on, change_note=change_note)
        print("The response of RawContractsApi->create_raw_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RawContractsApi->create_raw_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The PDF | 
 **coach_id** | **int**| The coach the document is filed for | 
 **school_id** | **int**| Optional. The school the document is filed under. Defaults to the coach&#39;s current school. | [optional] 
 **start_on** | **date**| Optional, YYYY-MM-DD. Together with end_on it also files a dated Coach contract (see above). | [optional] 
 **end_on** | **date**| Optional, YYYY-MM-DD, not before start_on. Required with start_on and refused without it. | [optional] 
 **change_note** | **str**| Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

### Return type

[**RawContractUploaded**](RawContractUploaded.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The RawContract was created and its text extraction queued |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to create RawContracts) |  -  |
**422** | The upload was refused (errors.file for a missing or non-PDF file, a file name longer than 255 characters or with a NUL character or bytes that are not UTF-8; errors.coach_id for a missing or unknown coach; errors.school_id for an unknown school; errors.start_on or errors.end_on for a malformed date, an end before the start or only one of the two; errors.change_note). Nothing was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

