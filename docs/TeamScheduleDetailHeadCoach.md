# TeamScheduleDetailHeadCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_detail_head_coach import TeamScheduleDetailHeadCoach

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleDetailHeadCoach from a JSON string
team_schedule_detail_head_coach_instance = TeamScheduleDetailHeadCoach.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleDetailHeadCoach.to_json())

# convert the object into a dict
team_schedule_detail_head_coach_dict = team_schedule_detail_head_coach_instance.to_dict()
# create an instance of TeamScheduleDetailHeadCoach from a dict
team_schedule_detail_head_coach_from_dict = TeamScheduleDetailHeadCoach.from_dict(team_schedule_detail_head_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


