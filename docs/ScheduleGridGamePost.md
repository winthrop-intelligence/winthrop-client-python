# ScheduleGridGamePost

Active game post for a grid school, trimmed for the grid view

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**game_types** | **List[str]** | Game type names (e.g. HomeAndHome, GuaranteeNeeded) | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_game_post import ScheduleGridGamePost

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridGamePost from a JSON string
schedule_grid_game_post_instance = ScheduleGridGamePost.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridGamePost.to_json())

# convert the object into a dict
schedule_grid_game_post_dict = schedule_grid_game_post_instance.to_dict()
# create an instance of ScheduleGridGamePost from a dict
schedule_grid_game_post_from_dict = ScheduleGridGamePost.from_dict(schedule_grid_game_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


