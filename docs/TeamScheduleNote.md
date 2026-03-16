# TeamScheduleNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_note import TeamScheduleNote

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleNote from a JSON string
team_schedule_note_instance = TeamScheduleNote.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleNote.to_json())

# convert the object into a dict
team_schedule_note_dict = team_schedule_note_instance.to_dict()
# create an instance of TeamScheduleNote from a dict
team_schedule_note_from_dict = TeamScheduleNote.from_dict(team_schedule_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


