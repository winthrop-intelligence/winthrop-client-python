# GetContractVerifications200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**data** | [**List[ContractVerification]**](ContractVerification.md) |  | 

## Example

```python
from winthrop_client_python.models.get_contract_verifications200_response import GetContractVerifications200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetContractVerifications200Response from a JSON string
get_contract_verifications200_response_instance = GetContractVerifications200Response.from_json(json)
# print the JSON string representation of the object
print(GetContractVerifications200Response.to_json())

# convert the object into a dict
get_contract_verifications200_response_dict = get_contract_verifications200_response_instance.to_dict()
# create an instance of GetContractVerifications200Response from a dict
get_contract_verifications200_response_from_dict = GetContractVerifications200Response.from_dict(get_contract_verifications200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


