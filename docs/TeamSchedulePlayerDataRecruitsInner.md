# TeamSchedulePlayerDataRecruitsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**height** | **str** |  | [optional] 
**weight** | **float** |  | [optional] 
**average_stars** | **float** |  | [optional] 
**overall_ranking** | **float** |  | [optional] 
**position_ranking** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_player_data_recruits_inner import TeamSchedulePlayerDataRecruitsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSchedulePlayerDataRecruitsInner from a JSON string
team_schedule_player_data_recruits_inner_instance = TeamSchedulePlayerDataRecruitsInner.from_json(json)
# print the JSON string representation of the object
print(TeamSchedulePlayerDataRecruitsInner.to_json())

# convert the object into a dict
team_schedule_player_data_recruits_inner_dict = team_schedule_player_data_recruits_inner_instance.to_dict()
# create an instance of TeamSchedulePlayerDataRecruitsInner from a dict
team_schedule_player_data_recruits_inner_from_dict = TeamSchedulePlayerDataRecruitsInner.from_dict(team_schedule_player_data_recruits_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


