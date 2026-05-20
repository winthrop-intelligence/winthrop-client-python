# ScheduleGridScheduleIntent

A private single-day /schedules grid marker (WINAD-9646). Not a public Games Wanted post.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**var_date** | **date** | The single cell date this marker applies to | [optional] 
**game_types** | **List[str]** | Game type names (e.g. HomeAndHome, GuaranteeNeeded, Pending) | [optional] 
**created_by_school_id** | **int** | School account ID that created this marker when entered by a school account; null for internal/admin/support or unknown sources | [optional] 
**school_entered** | **bool** | True when this marker was entered by a user from the owning school account | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_schedule_intent import ScheduleGridScheduleIntent

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridScheduleIntent from a JSON string
schedule_grid_schedule_intent_instance = ScheduleGridScheduleIntent.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridScheduleIntent.to_json())

# convert the object into a dict
schedule_grid_schedule_intent_dict = schedule_grid_schedule_intent_instance.to_dict()
# create an instance of ScheduleGridScheduleIntent from a dict
schedule_grid_schedule_intent_from_dict = ScheduleGridScheduleIntent.from_dict(schedule_grid_schedule_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


