# TeamScheduleDetailGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_display** | **str** |  | [optional] 
**opponent_id** | **int** |  | [optional] 
**opponent_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**opponent_rpi** | **int** |  | [optional] 
**opponent_avg_rpi** | **int** |  | [optional] 
**result** | **str** |  | [optional] 
**score** | **str** |  | [optional] 
**overtime** | **int** |  | [optional] 
**in_conference** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_detail_game import TeamScheduleDetailGame

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleDetailGame from a JSON string
team_schedule_detail_game_instance = TeamScheduleDetailGame.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleDetailGame.to_json())

# convert the object into a dict
team_schedule_detail_game_dict = team_schedule_detail_game_instance.to_dict()
# create an instance of TeamScheduleDetailGame from a dict
team_schedule_detail_game_from_dict = TeamScheduleDetailGame.from_dict(team_schedule_detail_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


