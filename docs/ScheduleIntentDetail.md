# ScheduleIntentDetail

A private /schedules grid marker (WINAD-9646). NOT a public Games Wanted post — never appears in the /game_posts feed, the school-detail badge, or the digest email.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**var_date** | **date** |  | [optional] 
**game_types** | [**List[ContactSearchCoachOptionsSportsInner]**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_intent_detail import ScheduleIntentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleIntentDetail from a JSON string
schedule_intent_detail_instance = ScheduleIntentDetail.from_json(json)
# print the JSON string representation of the object
print(ScheduleIntentDetail.to_json())

# convert the object into a dict
schedule_intent_detail_dict = schedule_intent_detail_instance.to_dict()
# create an instance of ScheduleIntentDetail from a dict
schedule_intent_detail_from_dict = ScheduleIntentDetail.from_dict(schedule_intent_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


