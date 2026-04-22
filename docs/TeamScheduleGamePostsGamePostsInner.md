# TeamScheduleGamePostsGamePostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**game_post_id** | **int** |  | [optional] 
**display_date** | **str** |  | [optional] 
**game_types** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**last_rpi** | **int** |  | [optional] 
**avg_rpi** | **int** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**distance** | **float** |  | [optional] 
**can_manage** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_game_posts_game_posts_inner import TeamScheduleGamePostsGamePostsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleGamePostsGamePostsInner from a JSON string
team_schedule_game_posts_game_posts_inner_instance = TeamScheduleGamePostsGamePostsInner.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleGamePostsGamePostsInner.to_json())

# convert the object into a dict
team_schedule_game_posts_game_posts_inner_dict = team_schedule_game_posts_game_posts_inner_instance.to_dict()
# create an instance of TeamScheduleGamePostsGamePostsInner from a dict
team_schedule_game_posts_game_posts_inner_from_dict = TeamScheduleGamePostsGamePostsInner.from_dict(team_schedule_game_posts_game_posts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


