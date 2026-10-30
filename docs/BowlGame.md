# BowlGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.bowl_game import BowlGame

# TODO update the JSON string below
json = "{}"
# create an instance of BowlGame from a JSON string
bowl_game_instance = BowlGame.from_json(json)
# print the JSON string representation of the object
print(BowlGame.to_json())

# convert the object into a dict
bowl_game_dict = bowl_game_instance.to_dict()
# create an instance of BowlGame from a dict
bowl_game_from_dict = BowlGame.from_dict(bowl_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


