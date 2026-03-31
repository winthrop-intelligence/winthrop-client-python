# TeamSchedulePlayerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_player_data** | **bool** |  | [optional] 
**season_label** | **str** |  | [optional] 
**import_date** | **str** |  | [optional] 
**returning_pct** | [**TeamSchedulePlayerDataReturningPct**](TeamSchedulePlayerDataReturningPct.md) |  | [optional] 
**returning_players** | [**List[TeamSchedulePlayerDataReturningPlayersInner]**](TeamSchedulePlayerDataReturningPlayersInner.md) |  | [optional] 
**departing_players** | [**List[TeamSchedulePlayerDataReturningPlayersInner]**](TeamSchedulePlayerDataReturningPlayersInner.md) |  | [optional] 
**recruits** | [**List[TeamSchedulePlayerDataRecruitsInner]**](TeamSchedulePlayerDataRecruitsInner.md) |  | [optional] 
**transfers** | [**List[TeamSchedulePlayerDataTransfersInner]**](TeamSchedulePlayerDataTransfersInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_player_data import TeamSchedulePlayerData

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSchedulePlayerData from a JSON string
team_schedule_player_data_instance = TeamSchedulePlayerData.from_json(json)
# print the JSON string representation of the object
print(TeamSchedulePlayerData.to_json())

# convert the object into a dict
team_schedule_player_data_dict = team_schedule_player_data_instance.to_dict()
# create an instance of TeamSchedulePlayerData from a dict
team_schedule_player_data_from_dict = TeamSchedulePlayerData.from_dict(team_schedule_player_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


