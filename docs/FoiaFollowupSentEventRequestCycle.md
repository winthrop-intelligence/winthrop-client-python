# FoiaFollowupSentEventRequestCycle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**follow_up_date** | **date** |  | 
**last_processed_followup** | **date** |  | 
**updated_at** | **datetime** | Echo the report updated_at exactly, including microseconds and an explicit offset or Z. | 

## Example

```python
from winthrop_client_python.models.foia_followup_sent_event_request_cycle import FoiaFollowupSentEventRequestCycle

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowupSentEventRequestCycle from a JSON string
foia_followup_sent_event_request_cycle_instance = FoiaFollowupSentEventRequestCycle.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowupSentEventRequestCycle.to_json())

# convert the object into a dict
foia_followup_sent_event_request_cycle_dict = foia_followup_sent_event_request_cycle_instance.to_dict()
# create an instance of FoiaFollowupSentEventRequestCycle from a dict
foia_followup_sent_event_request_cycle_from_dict = FoiaFollowupSentEventRequestCycle.from_dict(foia_followup_sent_event_request_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


