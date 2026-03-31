# TeamScheduleGamePosts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_own_school** | **bool** |  | [optional] 
**game_posts** | [**List[TeamScheduleGamePostsGamePostsInner]**](TeamScheduleGamePostsGamePostsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_game_posts import TeamScheduleGamePosts

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleGamePosts from a JSON string
team_schedule_game_posts_instance = TeamScheduleGamePosts.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleGamePosts.to_json())

# convert the object into a dict
team_schedule_game_posts_dict = team_schedule_game_posts_instance.to_dict()
# create an instance of TeamScheduleGamePosts from a dict
team_schedule_game_posts_from_dict = TeamScheduleGamePosts.from_dict(team_schedule_game_posts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


