# FoiaFollowUpReportRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request_id** | **int** |  | [optional] 
**foia_request_admin_url** | **str** |  | [optional] 
**school_admin_url** | **str** |  | [optional] 
**foia_label_id** | **int** |  | [optional] 
**foia_label_name** | **str** |  | [optional] 
**foia_request_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**status_label** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**fully_completed** | **bool** |  | [optional] 
**direct_contact** | **bool** |  | [optional] 
**direct_contact_started_at** | **datetime** |  | [optional] 
**completed_at** | **datetime** |  | [optional] 
**date_sent** | **date** |  | [optional] 
**days_to_receive_request** | **int** |  | [optional] 
**response_due_date** | **date** |  | [optional] 
**response_days_overdue** | **int** |  | [optional] 
**updated_by_school** | **date** |  | [optional] 
**last_comms_date_by_school** | **date** |  | [optional] 
**last_comms_date_by_school_source** | **str** |  | [optional] 
**days_since_last_comms_by_school** | **int** |  | [optional] 
**updated_by_wi** | **date** |  | [optional] 
**last_follow_up_sent_at** | **date** |  | [optional] 
**next_follow_up_date** | **date** |  | [optional] 
**follow_up_date** | **date** |  | [optional] 
**last_processed_followup** | **date** |  | [optional] 
**processed_today** | **bool** |  | [optional] 
**follow_up_email_text** | **str** |  | [optional] 
**follow_up_email_text_sha256** | **str** |  | [optional] 
**gmail_search_hints** | [**FoiaFollowUpGmailSearchHints**](FoiaFollowUpGmailSearchHints.md) |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**school_short_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**mail** | **bool** |  | [optional] 
**lawyer_sends** | **bool** |  | [optional] 
**portal_site** | **str** |  | [optional] 
**forms** | **bool** |  | [optional] 
**request_channel** | **str** |  | [optional] 
**normalized_request_channel** | **str** |  | [optional] 
**primary_foia_contact** | [**FoiaFollowUpContact**](FoiaFollowUpContact.md) |  | [optional] 
**lead_contacts** | [**List[FoiaFollowUpContact]**](FoiaFollowUpContact.md) |  | [optional] 
**cc_contacts** | [**List[FoiaFollowUpContact]**](FoiaFollowUpContact.md) |  | [optional] 
**all_foia_contacts** | [**List[FoiaFollowUpContact]**](FoiaFollowUpContact.md) |  | [optional] 
**escalation_contacts** | [**List[FoiaFollowUpContact]**](FoiaFollowUpContact.md) |  | [optional] 
**requested_items** | [**List[FoiaFollowUpRequestedItem]**](FoiaFollowUpRequestedItem.md) |  | [optional] 
**last_requested_item_received_at** | **datetime** |  | [optional] 
**received_items_last_7d_count** | **int** |  | [optional] 
**received_items_last_14d_count** | **int** |  | [optional] 
**received_items_last_30d_count** | **int** |  | [optional] 
**received_after_last_followup_count** | **int** |  | [optional] 
**recent_received_items** | [**List[FoiaFollowUpRecentReceivedItem]**](FoiaFollowUpRecentReceivedItem.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_follow_up_report_row import FoiaFollowUpReportRow

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpReportRow from a JSON string
foia_follow_up_report_row_instance = FoiaFollowUpReportRow.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpReportRow.to_json())

# convert the object into a dict
foia_follow_up_report_row_dict = foia_follow_up_report_row_instance.to_dict()
# create an instance of FoiaFollowUpReportRow from a dict
foia_follow_up_report_row_from_dict = FoiaFollowUpReportRow.from_dict(foia_follow_up_report_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


