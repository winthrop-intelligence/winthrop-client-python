# FoiaFollowupSentEventConflictCurrent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**updated_by_wi** | **date** |  | 
**last_processed_followup** | **date** |  | 
**follow_up_date** | **date** |  | 
**follow_up_date_explicit** | **bool** |  | 
**updated_at** | **datetime** | Echo the report updated_at exactly, including microseconds and an explicit offset or Z. | 

## Example

```python
from winthrop_client_python.models.foia_followup_sent_event_conflict_current import FoiaFollowupSentEventConflictCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowupSentEventConflictCurrent from a JSON string
foia_followup_sent_event_conflict_current_instance = FoiaFollowupSentEventConflictCurrent.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowupSentEventConflictCurrent.to_json())

# convert the object into a dict
foia_followup_sent_event_conflict_current_dict = foia_followup_sent_event_conflict_current_instance.to_dict()
# create an instance of FoiaFollowupSentEventConflictCurrent from a dict
foia_followup_sent_event_conflict_current_from_dict = FoiaFollowupSentEventConflictCurrent.from_dict(foia_followup_sent_event_conflict_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


