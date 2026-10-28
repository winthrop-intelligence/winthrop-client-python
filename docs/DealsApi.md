# winthrop_client_python.DealsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pending_deal**](DealsApi.md#create_pending_deal) | **POST** /api/v1/deals | 
[**delete_pending_deal**](DealsApi.md#delete_pending_deal) | **DELETE** /api/v1/deals/{dealId} | 
[**publish_pending_deal**](DealsApi.md#publish_pending_deal) | **POST** /api/v1/deals/{dealId}/publish | 


# **create_pending_deal**
> PendingDealCreated create_pending_deal(school_id, deal_type, file, vendor_id=vendor_id, drive_id=drive_id, change_note=change_note)

File a vendor deal PDF as a PENDING deal (WINAD-10698), the vendor counterpart of POST /contracts. In one transaction this creates a Deal with pending true (no dates, verified false, the optional vendor attached) and its RawContract (a vendor DEAL document linked to the deal and filed under the school, with the PDF attached); nothing is created and no file is left behind if the request is refused. The PDF must really be a PDF (its bytes are checked, not its name) and its file name at most 255 characters. The automatic OCR runs once after the upload; read the text with GET /raw_contracts/{raw_contractId}/ocr_text (Mistral on the first call, cached afterwards).

A pending deal is internal-only: it is not returned to customers by any search, list, show, export or MCP tool, and its PDF cannot be read by them. Staff list the pending deals with GET /deals?q[pending_eq]=true (or GET /deal_searches?q[pending_eq]=true) and delete one with DELETE /deals/{dealId}. Publishing is a separate operation. A pending deal does not change the school's deal status.

`deal_type` is one of Apparel, MMR (multimedia rights), Pouring, Concessions, Ticketing, Outsourced Ticketing, Trademark, Bookstore, Athletics Software (also `software`) or Travel (case, spaces and underscores do not matter), or the exact DealType name such as ApparelDealType. `drive_id` is the original Google Drive id of the source document, stored on the RawContract; a second request with the same drive_id for a deal of the same school is refused with 422 errors.drive_id. Requires the winad_write scope and a manage-level user (client-credentials service tokens included).


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.pending_deal_created import PendingDealCreated
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
    api_instance = winthrop_client_python.DealsApi(api_client)
    school_id = 56 # int | The school the deal is filed under
    deal_type = 'deal_type_example' # str | Apparel, MMR, Pouring, Concessions, Ticketing, Outsourced Ticketing, Trademark, Bookstore, Athletics Software or Travel (or the DealType name).
    file = None # bytearray | The contract PDF as a multipart upload.
    vendor_id = 56 # int | Optional. An existing vendor, attached to the deal. (optional)
    drive_id = 'drive_id_example' # str | Optional original Google Drive id of the source document; unique per school among deals. (optional)
    change_note = 'change_note_example' # str | Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. (optional)

    try:
        api_response = api_instance.create_pending_deal(school_id, deal_type, file, vendor_id=vendor_id, drive_id=drive_id, change_note=change_note)
        print("The response of DealsApi->create_pending_deal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealsApi->create_pending_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **school_id** | **int**| The school the deal is filed under | 
 **deal_type** | **str**| Apparel, MMR, Pouring, Concessions, Ticketing, Outsourced Ticketing, Trademark, Bookstore, Athletics Software or Travel (or the DealType name). | 
 **file** | **bytearray**| The contract PDF as a multipart upload. | 
 **vendor_id** | **int**| Optional. An existing vendor, attached to the deal. | [optional] 
 **drive_id** | **str**| Optional original Google Drive id of the source document; unique per school among deals. | [optional] 
 **change_note** | **str**| Optional. Why this change is being made, for the internal audit history. It is stored on every audit version this write creates, the records it saves as side effects included. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is written. Never returned by the write. | [optional] 

### Return type

[**PendingDealCreated**](PendingDealCreated.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The pending deal was created |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to create deals) |  -  |
**422** | The upload was refused (unknown school or vendor, unsupported deal type, missing or non-PDF file, a file name over 255 characters, with a NUL character or bytes that are not UTF-8, duplicate drive_id, invalid change_note). Nothing was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pending_deal**
> delete_pending_deal(deal_id, change_note=change_note)

Delete a vendor deal, only while it is pending (WINAD-10698). Also deletes its RawContract and the stored PDF (the file, its blob and attachment), so no file is left behind. A published deal, or a PDF that a coach contract or another record still uses, is refused with 422 and nothing is deleted. A pending deal is not found (404) for a caller who cannot read it. Requires the winad_write scope and a manage-level user.

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
    api_instance = winthrop_client_python.DealsApi(api_client)
    deal_id = 56 # int | ID of the pending Deal to delete
    change_note = 'change_note_example' # str | Optional. Why the record is being deleted, for the internal audit history; stored on every audit version the delete creates. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is deleted. Never returned. (optional)

    try:
        api_instance.delete_pending_deal(deal_id, change_note=change_note)
    except Exception as e:
        print("Exception when calling DealsApi->delete_pending_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deal_id** | **int**| ID of the pending Deal to delete | 
 **change_note** | **str**| Optional. Why the record is being deleted, for the internal audit history; stored on every audit version the delete creates. At most 500 characters after trimming; blank is the same as omitted; a value that is not text (a NUL character included) or is longer is refused with 422 (errors.change_note) before anything is deleted. Never returned. | [optional] 

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
**204** | The pending deal, its RawContract and its file were deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to delete deals) |  -  |
**404** | Not Found |  -  |
**422** | The deal is not pending (errors.base), its PDF is used by another record, or change_note is not text or is longer than 500 characters (errors.change_note). Nothing was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_pending_deal**
> DealUpdateResult publish_pending_deal(deal_id, publish_pending_deal_request)

Publish a pending vendor deal with the fields a person approved (WINAD-10699), the vendor counterpart of POST /contracts/{contractId}/publish. The deal is the one POST /deals filed from a vendor PDF (WINAD-10698); read the PDF text with GET /raw_contracts/{raw_contractId}/ocr_text, prepare the fields, have a person approve them, then send them here in ONE call. In one transaction, under the deal's row lock, this validates every field first and then writes the deal fields, the deal type's deal_detail and sets pending to false. If anything is refused nothing is written and the deal stays pending, so the request can be corrected and retried. Once published the deal appears in customer searches and its PDF becomes readable, like any deal entered in the admin, and the school's deal status is updated.

The body is the body of PATCH /deals/{dealId} (`deal` and `deal_detail`), checked by the same code: the same detail fields for every deal type (Apparel, MMR, Pouring, Concessions, Ticketing, Outsourced Ticketing, Trademark, Bookstore, NIL, Video Mgmt, Travel, Athletics Software), the same value rules, and an unknown field or one that belongs to another deal type is a 422 naming it (for example `deal_detail.srf`). Dates are plain calendar dates, strictly YYYY-MM-DD (WINAD-10687), stored as midnight UTC with no time-zone shift: send `start_on` / `end_on`, or `start_at` / `end_at` with the same plain date (a datetime is refused with 422; a `_at` and `_on` field of the same side together are refused). Also accepted in `deal`: `vendor_id`, the id of an existing vendor, which replaces the vendor the upload attached, and `autorenew`. `verified` and `archived` are not part of a publish and are refused.

A published deal minimally needs its school and deal type (set by the upload), an end date (`deal.end_on`) and at least one vendor (`deal.vendor_id`, unless the upload attached one). The start date, the detail values and the `change_note` are optional. A deal that is not pending (already published, entered in the admin, or published by an earlier call) is refused with 422 `errors.base`, so a second publish never changes anything. All problems are reported together, keyed by field path (`deal.end_on`, `deal.vendor_id`, `deal_detail.partner`, `base`). The change is audited with the acting user, the API client and the optional `change_note`, on the deal and on the detail it creates. The response is the published deal read back, in the shape of the PATCH response (`pending` is false). A pending deal is not found (404) for a caller who cannot read it. Requires the winad_write scope and a manage-level user (client-credentials service tokens included, as for POST /deals).


### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.deal_update_result import DealUpdateResult
from winthrop_client_python.models.publish_pending_deal_request import PublishPendingDealRequest
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
    api_instance = winthrop_client_python.DealsApi(api_client)
    deal_id = 56 # int | ID of the pending Deal to publish
    publish_pending_deal_request = winthrop_client_python.PublishPendingDealRequest() # PublishPendingDealRequest | 

    try:
        api_response = api_instance.publish_pending_deal(deal_id, publish_pending_deal_request)
        print("The response of DealsApi->publish_pending_deal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealsApi->publish_pending_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deal_id** | **int**| ID of the pending Deal to publish | 
 **publish_pending_deal_request** | [**PublishPendingDealRequest**](PublishPendingDealRequest.md)|  | 

### Return type

[**DealUpdateResult**](DealUpdateResult.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The deal was published and is read back from the database, with decimal fields returned as decimal strings. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden (missing winad_write scope or not permitted to update deals) |  -  |
**404** | Not Found (no such deal, or a pending one for a caller who cannot read it) |  -  |
**422** | The deal is not pending (errors.base), a field or value was refused (unknown or other-type fields, bad dates, a missing end date or vendor) or change_note is not text or is longer than 500 characters (errors.change_note). Nothing was written and the deal is still pending. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

