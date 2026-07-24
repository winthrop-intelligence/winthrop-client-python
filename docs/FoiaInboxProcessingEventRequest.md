# FoiaInboxProcessingEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_inbox_processing_event** | [**FoiaInboxProcessingEventInput**](FoiaInboxProcessingEventInput.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_processing_event_request import FoiaInboxProcessingEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxProcessingEventRequest from a JSON string
foia_inbox_processing_event_request_instance = FoiaInboxProcessingEventRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxProcessingEventRequest.to_json())

# convert the object into a dict
foia_inbox_processing_event_request_dict = foia_inbox_processing_event_request_instance.to_dict()
# create an instance of FoiaInboxProcessingEventRequest from a dict
foia_inbox_processing_event_request_from_dict = FoiaInboxProcessingEventRequest.from_dict(foia_inbox_processing_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


