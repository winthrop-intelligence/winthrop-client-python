# ListContractVerifications200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**data** | [**List[ContractVerification]**](ContractVerification.md) |  | 

## Example

```python
from winthrop_client_python.models.list_contract_verifications200_response import ListContractVerifications200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListContractVerifications200Response from a JSON string
list_contract_verifications200_response_instance = ListContractVerifications200Response.from_json(json)
# print the JSON string representation of the object
print(ListContractVerifications200Response.to_json())

# convert the object into a dict
list_contract_verifications200_response_dict = list_contract_verifications200_response_instance.to_dict()
# create an instance of ListContractVerifications200Response from a dict
list_contract_verifications200_response_from_dict = ListContractVerifications200Response.from_dict(list_contract_verifications200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


