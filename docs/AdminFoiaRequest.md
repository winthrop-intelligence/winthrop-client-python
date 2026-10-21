# AdminFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_sent** | **date** |  | [optional] 
**updated_by_school** | **str** |  | [optional] 
**updated_by_wi** | **date** |  | [optional] 
**follow_up_date** | **date** |  | [optional] 
**last_processed_followup** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**school** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**foia_label** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**requested_items_count** | **int** |  | [optional] 
**received_items_count** | **int** |  | [optional] 
**status_percentage** | **float** |  | [optional] 
**deal_status_ids** | **List[int]** |  | [optional] 
**foia_notes** | [**List[AdminFoiaRequestNote]**](AdminFoiaRequestNote.md) | Request-level notes, newest first; included on detail and write responses. | [optional] 
**vendor_options** | [**List[AdminFoiaVendorOption]**](AdminFoiaVendorOption.md) | FOIA-requestable vendor types for this school; reading does not create statuses. | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request import AdminFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequest from a JSON string
admin_foia_request_instance = AdminFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequest.to_json())

# convert the object into a dict
admin_foia_request_dict = admin_foia_request_instance.to_dict()
# create an instance of AdminFoiaRequest from a dict
admin_foia_request_from_dict = AdminFoiaRequest.from_dict(admin_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


