# GamePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**game_types** | [**List[GameType]**](GameType.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post import GamePost

# TODO update the JSON string below
json = "{}"
# create an instance of GamePost from a JSON string
game_post_instance = GamePost.from_json(json)
# print the JSON string representation of the object
print(GamePost.to_json())

# convert the object into a dict
game_post_dict = game_post_instance.to_dict()
# create an instance of GamePost from a dict
game_post_from_dict = GamePost.from_dict(game_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


