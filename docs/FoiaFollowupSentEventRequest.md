# FoiaFollowupSentEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cycle** | [**FoiaFollowupSentEventRequestCycle**](FoiaFollowupSentEventRequestCycle.md) |  | 
**expected_status** | **str** |  | 
**processed_on** | **date** |  | 
**idempotency_key** | **str** | Must not contain NUL characters. | 

## Example

```python
from winthrop_client_python.models.foia_followup_sent_event_request import FoiaFollowupSentEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowupSentEventRequest from a JSON string
foia_followup_sent_event_request_instance = FoiaFollowupSentEventRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowupSentEventRequest.to_json())

# convert the object into a dict
foia_followup_sent_event_request_dict = foia_followup_sent_event_request_instance.to_dict()
# create an instance of FoiaFollowupSentEventRequest from a dict
foia_followup_sent_event_request_from_dict = FoiaFollowupSentEventRequest.from_dict(foia_followup_sent_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


