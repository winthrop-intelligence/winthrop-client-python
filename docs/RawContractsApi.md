# winthrop_client_python.RawContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_raw_contract_contract_terms**](RawContractsApi.md#get_raw_contract_contract_terms) | **GET** /api/v1/raw_contracts/{raw_contractId}/contract_terms | 
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

# **update_raw_contract_contract_terms**
> RawContractTerms update_raw_contract_contract_terms(raw_contract_id, contract_terms)

Replace the whole contract_terms document on a RawContract (WINAD-10633). The body is the document itself: a JSON object with a `schema` string (for example "ticketing-terms-v1" or "coach-terms-v1") and a `source` object (`rendition_sha256`, `run_id`, `extracted_at`, `method`). Every other key is a term and is stored as sent; terms are not validated beyond the envelope. `source.rendition_sha256` is the SHA-256 (hex) of the OCR text the terms were read from (the `text` returned by GET /raw_contracts/{id}/ocr_text); when that text later changes, `contract_terms_stale` is true.

Every change is recorded in the audit trail (who, old and new value, when), so this requires the winad_write scope and a user-backed token (client-credentials tokens are refused) with permission to update the RawContract.


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

    try:
        api_response = api_instance.update_raw_contract_contract_terms(raw_contract_id, contract_terms)
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
**422** | The body is not a JSON object, or &#x60;schema&#x60; or &#x60;source&#x60; is missing or invalid. Nothing was changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

