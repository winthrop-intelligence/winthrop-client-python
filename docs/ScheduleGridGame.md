# ScheduleGridGame

A scheduled game for one of the grid's schools, viewed from that school's perspective

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**opponent_id** | **int** |  | [optional] 
**opponent_name** | **str** |  | [optional] 
**opponent_short_name** | **str** |  | [optional] 
**opponent_logo_url** | **str** |  | [optional] 
**is_home** | **bool** |  | [optional] 
**neutral** | **bool** |  | [optional] 
**guarantee_cents** | **int** | Associated game contract comp (cents), if any | [optional] 
**in_conference** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_game import ScheduleGridGame

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridGame from a JSON string
schedule_grid_game_instance = ScheduleGridGame.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridGame.to_json())

# convert the object into a dict
schedule_grid_game_dict = schedule_grid_game_instance.to_dict()
# create an instance of ScheduleGridGame from a dict
schedule_grid_game_from_dict = ScheduleGridGame.from_dict(schedule_grid_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


