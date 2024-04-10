# ContractCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Contract]**](Contract.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.contract_collection import ContractCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ContractCollection from a JSON string
contract_collection_instance = ContractCollection.from_json(json)
# print the JSON string representation of the object
print(ContractCollection.to_json())

# convert the object into a dict
contract_collection_dict = contract_collection_instance.to_dict()
# create an instance of ContractCollection from a dict
contract_collection_form_dict = contract_collection.from_dict(contract_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


