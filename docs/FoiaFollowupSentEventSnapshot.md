# FoiaFollowupSentEventSnapshot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**updated_by_wi** | **date** |  | 
**last_processed_followup** | **date** |  | 
**follow_up_date** | **date** |  | 
**follow_up_date_explicit** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.foia_followup_sent_event_snapshot import FoiaFollowupSentEventSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowupSentEventSnapshot from a JSON string
foia_followup_sent_event_snapshot_instance = FoiaFollowupSentEventSnapshot.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowupSentEventSnapshot.to_json())

# convert the object into a dict
foia_followup_sent_event_snapshot_dict = foia_followup_sent_event_snapshot_instance.to_dict()
# create an instance of FoiaFollowupSentEventSnapshot from a dict
foia_followup_sent_event_snapshot_from_dict = FoiaFollowupSentEventSnapshot.from_dict(foia_followup_sent_event_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


