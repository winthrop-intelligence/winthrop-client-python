# GameCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Game]**](Game.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_collection import GameCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GameCollection from a JSON string
game_collection_instance = GameCollection.from_json(json)
# print the JSON string representation of the object
print(GameCollection.to_json())

# convert the object into a dict
game_collection_dict = game_collection_instance.to_dict()
# create an instance of GameCollection from a dict
game_collection_form_dict = game_collection.from_dict(game_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


