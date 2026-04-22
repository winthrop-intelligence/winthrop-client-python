# GamePostDetailCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_detail_created_by import GamePostDetailCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostDetailCreatedBy from a JSON string
game_post_detail_created_by_instance = GamePostDetailCreatedBy.from_json(json)
# print the JSON string representation of the object
print(GamePostDetailCreatedBy.to_json())

# convert the object into a dict
game_post_detail_created_by_dict = game_post_detail_created_by_instance.to_dict()
# create an instance of GamePostDetailCreatedBy from a dict
game_post_detail_created_by_from_dict = GamePostDetailCreatedBy.from_dict(game_post_detail_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


