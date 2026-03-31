# TeamScheduleContact

Scheduling contact for a school/sport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** | Coach ID for linking to coach profile | [optional] 
**name** | **str** | Full name of the contact | [optional] 
**title** | **str** | Position title (e.g. Director of Football Operations) | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** | Formatted phone number | [optional] 
**avatar_url** | **str** | URL to coach avatar image (small cropped variant) | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_contact import TeamScheduleContact

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleContact from a JSON string
team_schedule_contact_instance = TeamScheduleContact.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleContact.to_json())

# convert the object into a dict
team_schedule_contact_dict = team_schedule_contact_instance.to_dict()
# create an instance of TeamScheduleContact from a dict
team_schedule_contact_from_dict = TeamScheduleContact.from_dict(team_schedule_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


