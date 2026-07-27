# FoiaInboxProcessingEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**mailbox** | **str** |  | 
**gmail_message_id** | **str** |  | 
**gmail_thread_id** | **str** |  | 
**run_id** | **str** |  | 
**foia_request_id** | **int** |  | 
**school_id** | **int** |  | 
**decision_sha256** | **str** |  | 
**request_sha256** | **str** |  | 
**status** | **str** |  | 
**applied_at** | **datetime** |  | 
**result** | **Dict[str, object]** |  | 
**idempotent** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_processing_event_response import FoiaInboxProcessingEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxProcessingEventResponse from a JSON string
foia_inbox_processing_event_response_instance = FoiaInboxProcessingEventResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxProcessingEventResponse.to_json())

# convert the object into a dict
foia_inbox_processing_event_response_dict = foia_inbox_processing_event_response_instance.to_dict()
# create an instance of FoiaInboxProcessingEventResponse from a dict
foia_inbox_processing_event_response_from_dict = FoiaInboxProcessingEventResponse.from_dict(foia_inbox_processing_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


