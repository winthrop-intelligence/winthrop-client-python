# TeamSchedulePlayerDataReturningPlayersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**player_class** | **str** |  | [optional] 
**pts** | **float** |  | [optional] 
**reb** | **float** |  | [optional] 
**ast** | **float** |  | [optional] 
**mpg** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_player_data_returning_players_inner import TeamSchedulePlayerDataReturningPlayersInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSchedulePlayerDataReturningPlayersInner from a JSON string
team_schedule_player_data_returning_players_inner_instance = TeamSchedulePlayerDataReturningPlayersInner.from_json(json)
# print the JSON string representation of the object
print(TeamSchedulePlayerDataReturningPlayersInner.to_json())

# convert the object into a dict
team_schedule_player_data_returning_players_inner_dict = team_schedule_player_data_returning_players_inner_instance.to_dict()
# create an instance of TeamSchedulePlayerDataReturningPlayersInner from a dict
team_schedule_player_data_returning_players_inner_from_dict = TeamSchedulePlayerDataReturningPlayersInner.from_dict(team_schedule_player_data_returning_players_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


