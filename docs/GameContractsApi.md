# winthrop_client_python.GameContractsApi

All URIs are relative to *http://api-gateway.default.svc.cluster.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_game_contract**](GameContractsApi.md#apply_game_contract) | **POST** /api/v1/game_contracts/apply | 


# **apply_game_contract**
> GameContractApplyResponse apply_game_contract(plan, raw_contract_file)

Atomically apply an approved game contract review plan — creates one RawContract for the uploaded PDF, one GameContract per approved action, and links each contract to its approved existing Games

### Example

* Api Key Authentication (ApiKey):
* OAuth Authentication (Oauth2):

```python
import winthrop_client_python
from winthrop_client_python.models.game_contract_apply_response import GameContractApplyResponse
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
    api_instance = winthrop_client_python.GameContractsApi(api_client)
    plan = 'plan_example' # str | JSON-encoded game-contract-entry-winad-plan/v1 review plan
    raw_contract_file = None # bytearray | The approved source contract PDF

    try:
        api_response = api_instance.apply_game_contract(plan, raw_contract_file)
        print("The response of GameContractsApi->apply_game_contract:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GameContractsApi->apply_game_contract: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan** | **str**| JSON-encoded game-contract-entry-winad-plan/v1 review plan | 
 **raw_contract_file** | **bytearray**| The approved source contract PDF | 

### Return type

[**GameContractApplyResponse**](GameContractApplyResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The approved plan was applied, or an exact retry was already applied |  -  |
**409** | A referenced Game changed after review, disappeared, or already has a GameContract |  -  |
**422** | Invalid plan, PDF, hashes, or GameContract values |  -  |
**503** | The configured game contract apply automation actor is unavailable |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

