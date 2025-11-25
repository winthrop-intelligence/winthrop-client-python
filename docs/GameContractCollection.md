# GameContractCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GameContract]**](GameContract.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_contract_collection import GameContractCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GameContractCollection from a JSON string
game_contract_collection_instance = GameContractCollection.from_json(json)
# print the JSON string representation of the object
print(GameContractCollection.to_json())

# convert the object into a dict
game_contract_collection_dict = game_contract_collection_instance.to_dict()
# create an instance of GameContractCollection from a dict
game_contract_collection_from_dict = GameContractCollection.from_dict(game_contract_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


