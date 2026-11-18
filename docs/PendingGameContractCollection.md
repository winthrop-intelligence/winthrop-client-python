# PendingGameContractCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PendingGameContract]**](PendingGameContract.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.pending_game_contract_collection import PendingGameContractCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractCollection from a JSON string
pending_game_contract_collection_instance = PendingGameContractCollection.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractCollection.to_json())

# convert the object into a dict
pending_game_contract_collection_dict = pending_game_contract_collection_instance.to_dict()
# create an instance of PendingGameContractCollection from a dict
pending_game_contract_collection_from_dict = PendingGameContractCollection.from_dict(pending_game_contract_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


