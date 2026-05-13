# ScheduleGridAvailableSchools

Response for GET /schedule_grid/{sport_name}/available_schools

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_count** | **int** | Total matching schools before the limit is applied | [optional] 
**schools** | [**List[ScheduleGridAvailableSchoolRow]**](ScheduleGridAvailableSchoolRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_available_schools import ScheduleGridAvailableSchools

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridAvailableSchools from a JSON string
schedule_grid_available_schools_instance = ScheduleGridAvailableSchools.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridAvailableSchools.to_json())

# convert the object into a dict
schedule_grid_available_schools_dict = schedule_grid_available_schools_instance.to_dict()
# create an instance of ScheduleGridAvailableSchools from a dict
schedule_grid_available_schools_from_dict = ScheduleGridAvailableSchools.from_dict(schedule_grid_available_schools_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


