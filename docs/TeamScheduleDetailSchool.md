# TeamScheduleDetailSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**conference_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_detail_school import TeamScheduleDetailSchool

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleDetailSchool from a JSON string
team_schedule_detail_school_instance = TeamScheduleDetailSchool.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleDetailSchool.to_json())

# convert the object into a dict
team_schedule_detail_school_dict = team_schedule_detail_school_instance.to_dict()
# create an instance of TeamScheduleDetailSchool from a dict
team_schedule_detail_school_from_dict = TeamScheduleDetailSchool.from_dict(team_schedule_detail_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


