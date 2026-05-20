# UpdateScheduleIntentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_intent** | [**UpdateScheduleIntentRequestScheduleIntent**](UpdateScheduleIntentRequestScheduleIntent.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_schedule_intent_request import UpdateScheduleIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleIntentRequest from a JSON string
update_schedule_intent_request_instance = UpdateScheduleIntentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleIntentRequest.to_json())

# convert the object into a dict
update_schedule_intent_request_dict = update_schedule_intent_request_instance.to_dict()
# create an instance of UpdateScheduleIntentRequest from a dict
update_schedule_intent_request_from_dict = UpdateScheduleIntentRequest.from_dict(update_schedule_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


