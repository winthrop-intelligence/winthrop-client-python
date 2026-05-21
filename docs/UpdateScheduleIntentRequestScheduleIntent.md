# UpdateScheduleIntentRequestScheduleIntent

Only game-type designations are mutable. sport_id and date identify the cell and are immutable after creation (WINAD-9646 security).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_schedule_intent_request_schedule_intent import UpdateScheduleIntentRequestScheduleIntent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleIntentRequestScheduleIntent from a JSON string
update_schedule_intent_request_schedule_intent_instance = UpdateScheduleIntentRequestScheduleIntent.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleIntentRequestScheduleIntent.to_json())

# convert the object into a dict
update_schedule_intent_request_schedule_intent_dict = update_schedule_intent_request_schedule_intent_instance.to_dict()
# create an instance of UpdateScheduleIntentRequestScheduleIntent from a dict
update_schedule_intent_request_schedule_intent_from_dict = UpdateScheduleIntentRequestScheduleIntent.from_dict(update_schedule_intent_request_schedule_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


