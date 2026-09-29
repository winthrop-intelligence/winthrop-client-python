# FoiaInboxApplyInputExpectedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**foia_label_id** | **int** |  | 
**updated_by_school** | **date** |  | 
**updated_by_wi** | **date** |  | 
**follow_up_date** | **date** | Required when the request effects set status, updated_by_wi, follow_up_date, or reset_follow_up_date. | [optional] 
**follow_up_date_explicit** | **bool** | Required when the request effects set follow_up_date or reset_follow_up_date. Rejects the write with 409 if the explicit marker changed since review, even when the calendar date is unchanged. | [optional] 
**updated_at** | **datetime** | Required when the request effects set follow_up_date or reset_follow_up_date. Revision token from the reviewed candidate row (microsecond precision); any intervening edit changes it, so a replayed payload cannot reapply a date over a later human correction and returns 409. A retry of a write that succeeded is still recognized from the resulting state and returns already_applied. | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_apply_input_expected_request import FoiaInboxApplyInputExpectedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxApplyInputExpectedRequest from a JSON string
foia_inbox_apply_input_expected_request_instance = FoiaInboxApplyInputExpectedRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxApplyInputExpectedRequest.to_json())

# convert the object into a dict
foia_inbox_apply_input_expected_request_dict = foia_inbox_apply_input_expected_request_instance.to_dict()
# create an instance of FoiaInboxApplyInputExpectedRequest from a dict
foia_inbox_apply_input_expected_request_from_dict = FoiaInboxApplyInputExpectedRequest.from_dict(foia_inbox_apply_input_expected_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


