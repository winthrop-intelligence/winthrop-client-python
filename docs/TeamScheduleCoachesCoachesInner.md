# TeamScheduleCoachesCoachesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**compensation** | **str** | Compensation label (e.g. &#39;Hourly&#39;) | [optional] 
**compensation_cents** | **int** | Total compensation in cents | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_coaches_coaches_inner import TeamScheduleCoachesCoachesInner

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleCoachesCoachesInner from a JSON string
team_schedule_coaches_coaches_inner_instance = TeamScheduleCoachesCoachesInner.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleCoachesCoachesInner.to_json())

# convert the object into a dict
team_schedule_coaches_coaches_inner_dict = team_schedule_coaches_coaches_inner_instance.to_dict()
# create an instance of TeamScheduleCoachesCoachesInner from a dict
team_schedule_coaches_coaches_inner_from_dict = TeamScheduleCoachesCoachesInner.from_dict(team_schedule_coaches_coaches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


