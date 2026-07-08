# FoiaRequestFollowUpHistoryRow

A single FOIA request follow-up-related change event sourced from PaperTrail versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request_id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**foia_label_id** | **int** |  | [optional] 
**foia_label_name** | **str** |  | [optional] 
**changed_at** | **datetime** |  | [optional] 
**changed_by_user_id** | **int** |  | [optional] 
**changed_by_user_name** | **str** |  | [optional] 
**previous_status** | **str** |  | [optional] 
**new_status** | **str** |  | [optional] 
**previous_updated_by_wi** | **date** |  | [optional] 
**new_updated_by_wi** | **date** |  | [optional] 
**previous_follow_up_date** | **date** |  | [optional] 
**new_follow_up_date** | **date** |  | [optional] 
**previous_last_processed_followup** | **date** |  | [optional] 
**new_last_processed_followup** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_request_follow_up_history_row import FoiaRequestFollowUpHistoryRow

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaRequestFollowUpHistoryRow from a JSON string
foia_request_follow_up_history_row_instance = FoiaRequestFollowUpHistoryRow.from_json(json)
# print the JSON string representation of the object
print(FoiaRequestFollowUpHistoryRow.to_json())

# convert the object into a dict
foia_request_follow_up_history_row_dict = foia_request_follow_up_history_row_instance.to_dict()
# create an instance of FoiaRequestFollowUpHistoryRow from a dict
foia_request_follow_up_history_row_from_dict = FoiaRequestFollowUpHistoryRow.from_dict(foia_request_follow_up_history_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


