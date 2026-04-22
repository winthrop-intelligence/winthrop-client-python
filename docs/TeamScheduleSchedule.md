# TeamScheduleSchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**games** | [**List[TeamScheduleScheduleGamesInner]**](TeamScheduleScheduleGamesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_schedule import TeamScheduleSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleSchedule from a JSON string
team_schedule_schedule_instance = TeamScheduleSchedule.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleSchedule.to_json())

# convert the object into a dict
team_schedule_schedule_dict = team_schedule_schedule_instance.to_dict()
# create an instance of TeamScheduleSchedule from a dict
team_schedule_schedule_from_dict = TeamScheduleSchedule.from_dict(team_schedule_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


