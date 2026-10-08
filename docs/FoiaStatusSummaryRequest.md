# FoiaStatusSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request_id** | **int** |  | 
**foia_request_admin_url** | **str** |  | 
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**foia_label_id** | **int** |  | 
**foia_label_name** | **str** |  | 
**lifecycle_status** | **str** |  | 
**request_status** | **str** | FoiaRequest status (request level, not item level). partial exists only here. | 
**next_update_due_on** | **date** | Raw follow_up_date for active requests; null for closed requests or missing dates (see data_gaps). | 
**follow_up_due_on** | **date** | Present only while the request remains eligible under the existing due follow-up rules. Null for completed, direct_contact and processed-today requests, but next_update_due_on still shows the date. | 
**updated_by_school** | **date** |  | 
**updated_by_wi** | **date** |  | 
**last_processed_followup** | **date** |  | 
**requested_items** | [**List[FoiaStatusSummaryRequestedItem]**](FoiaStatusSummaryRequestedItem.md) |  | 
**active_hold_reason** | **str** | Reason code of the recognized hold note, or null when the latest note is not a recognized hold. Populated from the latest note regardless of lifecycle. | 
**active_hold_justified** | **bool** | true when an active request has a recognized hold note, false when an active request has no recognized hold, null for closed requests. | 
**active_hold_note_id** | **int** | Recognized hold note ID from the latest note regardless of lifecycle; otherwise null. | 
**active_hold_note_excerpt** | **str** | The exact concise, closed-vocabulary hold note when one is recognized, populated from the latest note regardless of lifecycle; arbitrary note text is not exposed. | 
**flags** | [**FoiaStatusSummaryFlags**](FoiaStatusSummaryFlags.md) |  | 
**flag_reasons** | **List[str]** |  | 
**data_gaps** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.foia_status_summary_request import FoiaStatusSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaStatusSummaryRequest from a JSON string
foia_status_summary_request_instance = FoiaStatusSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaStatusSummaryRequest.to_json())

# convert the object into a dict
foia_status_summary_request_dict = foia_status_summary_request_instance.to_dict()
# create an instance of FoiaStatusSummaryRequest from a dict
foia_status_summary_request_from_dict = FoiaStatusSummaryRequest.from_dict(foia_status_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


