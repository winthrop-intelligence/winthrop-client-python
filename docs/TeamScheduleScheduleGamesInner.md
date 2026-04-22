# TeamScheduleScheduleGamesInner


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
**in_conference** | **bool** |  | [optional] 
**has_contract** | **bool** |  | [optional] 
**compensation_cents** | **int** |  | [optional] 
**game_contract_id** | **int** |  | [optional] 
**result** | **str** |  | [optional] 
**score** | **str** |  | [optional] 
**overtime** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_schedule_games_inner import TeamScheduleScheduleGamesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleScheduleGamesInner from a JSON string
team_schedule_schedule_games_inner_instance = TeamScheduleScheduleGamesInner.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleScheduleGamesInner.to_json())

# convert the object into a dict
team_schedule_schedule_games_inner_dict = team_schedule_schedule_games_inner_instance.to_dict()
# create an instance of TeamScheduleScheduleGamesInner from a dict
team_schedule_schedule_games_inner_from_dict = TeamScheduleScheduleGamesInner.from_dict(team_schedule_schedule_games_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


