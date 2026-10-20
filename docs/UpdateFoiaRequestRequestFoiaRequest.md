# UpdateFoiaRequestRequestFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**foia_label_id** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**date_sent** | **date** |  | [optional] 
**updated_by_wi** | **date** |  | [optional] 
**follow_up_date** | **date** |  | [optional] 
**updated_by_school** | **date** |  | [optional] 
**deal_status_ids** | **List[int]** |  | [optional] 
**foia_notes_attributes** | [**List[UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner]**](UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner.md) | Request-level note edits. Omit id to add; pass id to edit or delete. Author is set by the server. | [optional] 
**vendor_deal_type_ids** | **List[int]** | Add these FOIA-requestable types without replacing existing requested items. Idempotent. | [optional] 
**school_foia_notes_attributes** | [**List[UpdateFoiaRequestRequestFoiaRequestSchoolFoiaNotesAttributesInner]**](UpdateFoiaRequestRequestFoiaRequestSchoolFoiaNotesAttributesInner.md) | Notes scoped to this request&#39;s school. Author is set by the server; foreign note IDs are refused. | [optional] 

## Example

```python
from winthrop_client_python.models.update_foia_request_request_foia_request import UpdateFoiaRequestRequestFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFoiaRequestRequestFoiaRequest from a JSON string
update_foia_request_request_foia_request_instance = UpdateFoiaRequestRequestFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFoiaRequestRequestFoiaRequest.to_json())

# convert the object into a dict
update_foia_request_request_foia_request_dict = update_foia_request_request_foia_request_instance.to_dict()
# create an instance of UpdateFoiaRequestRequestFoiaRequest from a dict
update_foia_request_request_foia_request_from_dict = UpdateFoiaRequestRequestFoiaRequest.from_dict(update_foia_request_request_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


