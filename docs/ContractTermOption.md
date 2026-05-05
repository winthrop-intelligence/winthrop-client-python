# ContractTermOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.contract_term_option import ContractTermOption

# TODO update the JSON string below
json = "{}"
# create an instance of ContractTermOption from a JSON string
contract_term_option_instance = ContractTermOption.from_json(json)
# print the JSON string representation of the object
print(ContractTermOption.to_json())

# convert the object into a dict
contract_term_option_dict = contract_term_option_instance.to_dict()
# create an instance of ContractTermOption from a dict
contract_term_option_from_dict = ContractTermOption.from_dict(contract_term_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


