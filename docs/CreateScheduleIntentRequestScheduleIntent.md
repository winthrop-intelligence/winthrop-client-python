# CreateScheduleIntentRequestScheduleIntent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**var_date** | **date** |  | 
**game_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_schedule_intent_request_schedule_intent import CreateScheduleIntentRequestScheduleIntent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleIntentRequestScheduleIntent from a JSON string
create_schedule_intent_request_schedule_intent_instance = CreateScheduleIntentRequestScheduleIntent.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleIntentRequestScheduleIntent.to_json())

# convert the object into a dict
create_schedule_intent_request_schedule_intent_dict = create_schedule_intent_request_schedule_intent_instance.to_dict()
# create an instance of CreateScheduleIntentRequestScheduleIntent from a dict
create_schedule_intent_request_schedule_intent_from_dict = CreateScheduleIntentRequestScheduleIntent.from_dict(create_schedule_intent_request_schedule_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


