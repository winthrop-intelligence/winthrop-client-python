# ContractHistoryCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**data** | [**List[ContractHistoryEntry]**](ContractHistoryEntry.md) |  | 

## Example

```python
from winthrop_client_python.models.contract_history_collection import ContractHistoryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ContractHistoryCollection from a JSON string
contract_history_collection_instance = ContractHistoryCollection.from_json(json)
# print the JSON string representation of the object
print(ContractHistoryCollection.to_json())

# convert the object into a dict
contract_history_collection_dict = contract_history_collection_instance.to_dict()
# create an instance of ContractHistoryCollection from a dict
contract_history_collection_from_dict = ContractHistoryCollection.from_dict(contract_history_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


