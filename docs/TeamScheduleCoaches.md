# TeamScheduleCoaches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**performance_year** | **int** |  | [optional] 
**performance_years** | **List[int]** |  | [optional] 
**coaches** | [**List[TeamScheduleCoachesCoachesInner]**](TeamScheduleCoachesCoachesInner.md) |  | [optional] 
**head_coaches** | **List[List[GetFavoritesCategories200ResponseInner]]** |  | [optional] 
**seasons** | [**List[TeamScheduleCoachesSeasonsInner]**](TeamScheduleCoachesSeasonsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_coaches import TeamScheduleCoaches

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleCoaches from a JSON string
team_schedule_coaches_instance = TeamScheduleCoaches.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleCoaches.to_json())

# convert the object into a dict
team_schedule_coaches_dict = team_schedule_coaches_instance.to_dict()
# create an instance of TeamScheduleCoaches from a dict
team_schedule_coaches_from_dict = TeamScheduleCoaches.from_dict(team_schedule_coaches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


