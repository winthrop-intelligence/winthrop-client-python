# CtbGraduateAssistantCompensationApplyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_series_id** | **str** |  | 
**review_revision_sha256** | **str** |  | 
**decision_sha256** | **str** |  | 
**foia_request_id** | **int** |  | 
**school_id** | **int** |  | 
**requested_item_id** | **int** |  | 
**compensation_id** | **int** |  | 
**role** | **str** | CTB compensation-availability interpretation selected in the reviewed decision. | 
**actions** | **List[str]** | Granular actions approved for the reviewed graduate-assistant exception. | 
**requested_item_note** | **str** | Exact reviewed entry to append when add_requested_item_note is selected. | [optional] 
**compensation_comment** | **str** | Exact reviewed sentence to append when add_compensation_note is selected. | [optional] 
**position_ids** | **List[int]** | Reviewed compensation positions to update when add_position_type is selected. | [optional] 
**expected_request** | [**CtbCompensationExpectedRequest**](CtbCompensationExpectedRequest.md) |  | 
**expected_requested_item** | [**FoiaInboxExpectedRequestedItem**](FoiaInboxExpectedRequestedItem.md) |  | 
**expected_compensation** | [**FoiaInboxExpectedCompensation**](FoiaInboxExpectedCompensation.md) |  | 

## Example

```python
from winthrop_client_python.models.ctb_graduate_assistant_compensation_apply_input import CtbGraduateAssistantCompensationApplyInput

# TODO update the JSON string below
json = "{}"
# create an instance of CtbGraduateAssistantCompensationApplyInput from a JSON string
ctb_graduate_assistant_compensation_apply_input_instance = CtbGraduateAssistantCompensationApplyInput.from_json(json)
# print the JSON string representation of the object
print(CtbGraduateAssistantCompensationApplyInput.to_json())

# convert the object into a dict
ctb_graduate_assistant_compensation_apply_input_dict = ctb_graduate_assistant_compensation_apply_input_instance.to_dict()
# create an instance of CtbGraduateAssistantCompensationApplyInput from a dict
ctb_graduate_assistant_compensation_apply_input_from_dict = CtbGraduateAssistantCompensationApplyInput.from_dict(ctb_graduate_assistant_compensation_apply_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


