# ScheduleGridAvailableSchoolRow

Candidate school returned by the available-schools finder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**primary_contact_name** | **str** |  | [optional] 
**primary_contact_phone** | **str** |  | [optional] 
**subdivision_name** | **str** |  | [optional] 
**rank** | **int** | Current USNWR ranking (omitted when blank) | [optional] 
**distance_miles** | **int** | Distance from user_school_id in miles (omitted when distance filtering is not active) | [optional] 
**nearest_post** | [**ScheduleGridAvailableSchoolPost**](ScheduleGridAvailableSchoolPost.md) | Nearest active GamePost to target_date in the window. Null when the school has no openness recorded for the window (assumed-eligible). | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_available_school_row import ScheduleGridAvailableSchoolRow

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridAvailableSchoolRow from a JSON string
schedule_grid_available_school_row_instance = ScheduleGridAvailableSchoolRow.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridAvailableSchoolRow.to_json())

# convert the object into a dict
schedule_grid_available_school_row_dict = schedule_grid_available_school_row_instance.to_dict()
# create an instance of ScheduleGridAvailableSchoolRow from a dict
schedule_grid_available_school_row_from_dict = ScheduleGridAvailableSchoolRow.from_dict(schedule_grid_available_school_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


