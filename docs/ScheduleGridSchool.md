# ScheduleGridSchool

One of the up-to-eight schools rendered as a column on the schedule grid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**primary_contact_name** | **str** |  | [optional] 
**primary_contact_email** | **str** |  | [optional] 
**primary_contact_phone** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_school import ScheduleGridSchool

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridSchool from a JSON string
schedule_grid_school_instance = ScheduleGridSchool.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridSchool.to_json())

# convert the object into a dict
schedule_grid_school_dict = schedule_grid_school_instance.to_dict()
# create an instance of ScheduleGridSchool from a dict
schedule_grid_school_from_dict = ScheduleGridSchool.from_dict(schedule_grid_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


