# ScheduleGridAvailableSchoolPost

The game post nearest to the requested target_date for an available school

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**game_types** | **List[str]** |  | [optional] 
**primary_deal_type** | **str** | First matching deal type in priority order (HomeAndHome, GuaranteeOffered, GuaranteeNeeded, Tournament, Neutral) | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_available_school_post import ScheduleGridAvailableSchoolPost

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridAvailableSchoolPost from a JSON string
schedule_grid_available_school_post_instance = ScheduleGridAvailableSchoolPost.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridAvailableSchoolPost.to_json())

# convert the object into a dict
schedule_grid_available_school_post_dict = schedule_grid_available_school_post_instance.to_dict()
# create an instance of ScheduleGridAvailableSchoolPost from a dict
schedule_grid_available_school_post_from_dict = ScheduleGridAvailableSchoolPost.from_dict(schedule_grid_available_school_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


