# ScheduleGridView

Schedule grid payload for a single sport and season

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**season_start** | **date** | First Monday of November of the calendar year before the season year (e.g. Nov 2026 for season year 2027) | [optional] 
**season_end** | **date** | December 31 of the calendar year before the season year (e.g. Dec 31 2026 for season year 2027) | [optional] 
**schools** | [**List[ScheduleGridSchool]**](ScheduleGridSchool.md) |  | [optional] 
**games** | **Dict[str, List[ScheduleGridGame]]** | Games keyed by school_id (as a string). Each school&#39;s list is filtered to games where that school is home or away. | [optional] 
**schedule_intents** | **Dict[str, List[ScheduleGridScheduleIntent]]** | Private single-day grid markers keyed by school_id (as a string) | [optional] 
**schedule_tournaments** | **Dict[str, List[ScheduleGridScheduleTournament]]** | Private single-day multi-team event (MTE) placeholders keyed by school_id (as a string). Always present; completed seasons emit an empty object. | [optional] 
**onboarding** | [**ScheduleGridOnboarding**](ScheduleGridOnboarding.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_view import ScheduleGridView

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridView from a JSON string
schedule_grid_view_instance = ScheduleGridView.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridView.to_json())

# convert the object into a dict
schedule_grid_view_dict = schedule_grid_view_instance.to_dict()
# create an instance of ScheduleGridView from a dict
schedule_grid_view_from_dict = ScheduleGridView.from_dict(schedule_grid_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


