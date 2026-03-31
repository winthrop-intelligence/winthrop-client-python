# TeamScheduleCoachesSeasonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**rpi** | **int** |  | [optional] 
**record_str** | **str** |  | [optional] 
**conference_record** | **str** |  | [optional] 
**postseason** | **str** |  | [optional] 
**home_record** | **str** |  | [optional] 
**home_win_percent** | **float** |  | [optional] 
**sos_ranking** | **int** |  | [optional] 
**offensive_efficiency** | **float** |  | [optional] 
**defensive_efficiency** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_coaches_seasons_inner import TeamScheduleCoachesSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleCoachesSeasonsInner from a JSON string
team_schedule_coaches_seasons_inner_instance = TeamScheduleCoachesSeasonsInner.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleCoachesSeasonsInner.to_json())

# convert the object into a dict
team_schedule_coaches_seasons_inner_dict = team_schedule_coaches_seasons_inner_instance.to_dict()
# create an instance of TeamScheduleCoachesSeasonsInner from a dict
team_schedule_coaches_seasons_inner_from_dict = TeamScheduleCoachesSeasonsInner.from_dict(team_schedule_coaches_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


