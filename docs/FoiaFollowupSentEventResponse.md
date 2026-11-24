# FoiaFollowupSentEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request_id** | **int** |  | 
**idempotency_key** | **str** |  | 
**before** | [**FoiaFollowupSentEventSnapshot**](FoiaFollowupSentEventSnapshot.md) |  | 
**after** | [**FoiaFollowupSentEventSnapshot**](FoiaFollowupSentEventSnapshot.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_followup_sent_event_response import FoiaFollowupSentEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowupSentEventResponse from a JSON string
foia_followup_sent_event_response_instance = FoiaFollowupSentEventResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowupSentEventResponse.to_json())

# convert the object into a dict
foia_followup_sent_event_response_dict = foia_followup_sent_event_response_instance.to_dict()
# create an instance of FoiaFollowupSentEventResponse from a dict
foia_followup_sent_event_response_from_dict = FoiaFollowupSentEventResponse.from_dict(foia_followup_sent_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


