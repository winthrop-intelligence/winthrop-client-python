# ContractFileReplaced


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The contract&#39;s id | 
**raw_contract_id** | **int** | The id of the RawContract that now holds the new PDF | 
**filename** | **str** | The uploaded PDF&#39;s filename | 
**coach_id** | **int** |  | 
**pending** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.contract_file_replaced import ContractFileReplaced

# TODO update the JSON string below
json = "{}"
# create an instance of ContractFileReplaced from a JSON string
contract_file_replaced_instance = ContractFileReplaced.from_json(json)
# print the JSON string representation of the object
print(ContractFileReplaced.to_json())

# convert the object into a dict
contract_file_replaced_dict = contract_file_replaced_instance.to_dict()
# create an instance of ContractFileReplaced from a dict
contract_file_replaced_from_dict = ContractFileReplaced.from_dict(contract_file_replaced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


