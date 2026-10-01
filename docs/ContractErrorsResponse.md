# ContractErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** | Error messages keyed by attribute (base for whole-request errors) | 

## Example

```python
from winthrop_client_python.models.contract_errors_response import ContractErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContractErrorsResponse from a JSON string
contract_errors_response_instance = ContractErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(ContractErrorsResponse.to_json())

# convert the object into a dict
contract_errors_response_dict = contract_errors_response_instance.to_dict()
# create an instance of ContractErrorsResponse from a dict
contract_errors_response_from_dict = ContractErrorsResponse.from_dict(contract_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


