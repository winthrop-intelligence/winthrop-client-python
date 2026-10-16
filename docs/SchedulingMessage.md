# SchedulingMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**source** | **str** |  | 
**status** | **str** |  | 
**recipient_email** | **str** |  | 

## Example

```python
from winthrop_client_python.models.scheduling_message import SchedulingMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulingMessage from a JSON string
scheduling_message_instance = SchedulingMessage.from_json(json)
# print the JSON string representation of the object
print(SchedulingMessage.to_json())

# convert the object into a dict
scheduling_message_dict = scheduling_message_instance.to_dict()
# create an instance of SchedulingMessage from a dict
scheduling_message_from_dict = SchedulingMessage.from_dict(scheduling_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


