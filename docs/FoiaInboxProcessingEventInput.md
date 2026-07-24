# FoiaInboxProcessingEventInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox** | **str** |  | 
**gmail_message_id** | **str** |  | 
**gmail_thread_id** | **str** |  | 
**run_id** | **str** |  | 
**foia_request_id** | **int** |  | 
**school_id** | **int** |  | 
**decision_sha256** | **str** |  | 
**expected_request** | [**FoiaInboxProcessingEventInputExpectedRequest**](FoiaInboxProcessingEventInputExpectedRequest.md) |  | 
**effects** | [**FoiaInboxEffects**](FoiaInboxEffects.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_processing_event_input import FoiaInboxProcessingEventInput

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxProcessingEventInput from a JSON string
foia_inbox_processing_event_input_instance = FoiaInboxProcessingEventInput.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxProcessingEventInput.to_json())

# convert the object into a dict
foia_inbox_processing_event_input_dict = foia_inbox_processing_event_input_instance.to_dict()
# create an instance of FoiaInboxProcessingEventInput from a dict
foia_inbox_processing_event_input_from_dict = FoiaInboxProcessingEventInput.from_dict(foia_inbox_processing_event_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


