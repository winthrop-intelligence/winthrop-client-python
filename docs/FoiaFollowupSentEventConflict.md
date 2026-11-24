# FoiaFollowupSentEventConflict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**reasons** | **List[str]** |  | 
**current** | [**FoiaFollowupSentEventConflictCurrent**](FoiaFollowupSentEventConflictCurrent.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_followup_sent_event_conflict import FoiaFollowupSentEventConflict

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowupSentEventConflict from a JSON string
foia_followup_sent_event_conflict_instance = FoiaFollowupSentEventConflict.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowupSentEventConflict.to_json())

# convert the object into a dict
foia_followup_sent_event_conflict_dict = foia_followup_sent_event_conflict_instance.to_dict()
# create an instance of FoiaFollowupSentEventConflict from a dict
foia_followup_sent_event_conflict_from_dict = FoiaFollowupSentEventConflict.from_dict(foia_followup_sent_event_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


