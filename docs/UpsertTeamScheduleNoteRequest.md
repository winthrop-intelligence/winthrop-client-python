# UpsertTeamScheduleNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 

## Example

```python
from winthrop_client_python.models.upsert_team_schedule_note_request import UpsertTeamScheduleNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertTeamScheduleNoteRequest from a JSON string
upsert_team_schedule_note_request_instance = UpsertTeamScheduleNoteRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertTeamScheduleNoteRequest.to_json())

# convert the object into a dict
upsert_team_schedule_note_request_dict = upsert_team_schedule_note_request_instance.to_dict()
# create an instance of UpsertTeamScheduleNoteRequest from a dict
upsert_team_schedule_note_request_from_dict = UpsertTeamScheduleNoteRequest.from_dict(upsert_team_schedule_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


