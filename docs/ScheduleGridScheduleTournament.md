# ScheduleGridScheduleTournament

A private single-day /schedules grid multi-team event (MTE) placeholder (WINAD-9818). Rendered as \"Tournament Name (MTE)\" in the cell.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_date** | **date** | The single cell date this tournament applies to | [optional] 
**name** | **str** | Tournament name (e.g. \&quot;Maui Invitational\&quot;) | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_schedule_tournament import ScheduleGridScheduleTournament

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridScheduleTournament from a JSON string
schedule_grid_schedule_tournament_instance = ScheduleGridScheduleTournament.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridScheduleTournament.to_json())

# convert the object into a dict
schedule_grid_schedule_tournament_dict = schedule_grid_schedule_tournament_instance.to_dict()
# create an instance of ScheduleGridScheduleTournament from a dict
schedule_grid_schedule_tournament_from_dict = ScheduleGridScheduleTournament.from_dict(schedule_grid_schedule_tournament_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


