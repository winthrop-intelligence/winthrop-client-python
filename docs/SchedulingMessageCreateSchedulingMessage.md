# SchedulingMessageCreateSchedulingMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**source** | **str** |  | 
**recipient_email** | **str** |  | 
**contact_id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**publish_group_id** | **UUID** |  | [optional] 

## Example

```python
from winthrop_client_python.models.scheduling_message_create_scheduling_message import SchedulingMessageCreateSchedulingMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingMessageCreateSchedulingMessage from a JSON string
scheduling_message_create_scheduling_message_instance = SchedulingMessageCreateSchedulingMessage.from_json(json)
# print the JSON string representation of the object
print(SchedulingMessageCreateSchedulingMessage.to_json())

# convert the object into a dict
scheduling_message_create_scheduling_message_dict = scheduling_message_create_scheduling_message_instance.to_dict()
# create an instance of SchedulingMessageCreateSchedulingMessage from a dict
scheduling_message_create_scheduling_message_from_dict = SchedulingMessageCreateSchedulingMessage.from_dict(scheduling_message_create_scheduling_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


