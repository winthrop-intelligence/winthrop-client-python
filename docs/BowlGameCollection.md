# BowlGameCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BowlGame]**](BowlGame.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.bowl_game_collection import BowlGameCollection

# TODO update the JSON string below
json = "{}"
# create an instance of BowlGameCollection from a JSON string
bowl_game_collection_instance = BowlGameCollection.from_json(json)
# print the JSON string representation of the object
print(BowlGameCollection.to_json())

# convert the object into a dict
bowl_game_collection_dict = bowl_game_collection_instance.to_dict()
# create an instance of BowlGameCollection from a dict
bowl_game_collection_from_dict = BowlGameCollection.from_dict(bowl_game_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


