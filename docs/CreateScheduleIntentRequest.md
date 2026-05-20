# CreateScheduleIntentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_intent** | [**CreateScheduleIntentRequestScheduleIntent**](CreateScheduleIntentRequestScheduleIntent.md) |  | 

## Example

```python
from winthrop_client_python.models.create_schedule_intent_request import CreateScheduleIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleIntentRequest from a JSON string
create_schedule_intent_request_instance = CreateScheduleIntentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleIntentRequest.to_json())

# convert the object into a dict
create_schedule_intent_request_dict = create_schedule_intent_request_instance.to_dict()
# create an instance of CreateScheduleIntentRequest from a dict
create_schedule_intent_request_from_dict = CreateScheduleIntentRequest.from_dict(create_schedule_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


