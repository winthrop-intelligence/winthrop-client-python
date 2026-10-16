# SchedulingMessageCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduling_message** | [**SchedulingMessageCreateSchedulingMessage**](SchedulingMessageCreateSchedulingMessage.md) |  | 

## Example

```python
from winthrop_client_python.models.scheduling_message_create import SchedulingMessageCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingMessageCreate from a JSON string
scheduling_message_create_instance = SchedulingMessageCreate.from_json(json)
# print the JSON string representation of the object
print(SchedulingMessageCreate.to_json())

# convert the object into a dict
scheduling_message_create_dict = scheduling_message_create_instance.to_dict()
# create an instance of SchedulingMessageCreate from a dict
scheduling_message_create_from_dict = SchedulingMessageCreate.from_dict(scheduling_message_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


