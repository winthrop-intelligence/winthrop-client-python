# GameType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_type import GameType

# TODO update the JSON string below
json = "{}"
# create an instance of GameType from a JSON string
game_type_instance = GameType.from_json(json)
# print the JSON string representation of the object
print(GameType.to_json())

# convert the object into a dict
game_type_dict = game_type_instance.to_dict()
# create an instance of GameType from a dict
game_type_from_dict = GameType.from_dict(game_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


