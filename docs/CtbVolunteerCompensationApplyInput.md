# CtbVolunteerCompensationApplyInput


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
**actions** | **List[str]** | Granular actions approved for the reviewed volunteer exception. | 
**expected_request** | [**CtbCompensationExpectedRequest**](CtbCompensationExpectedRequest.md) |  | 
**expected_requested_item** | [**FoiaInboxExpectedRequestedItem**](FoiaInboxExpectedRequestedItem.md) |  | 
**expected_compensation** | [**FoiaInboxExpectedCompensation**](FoiaInboxExpectedCompensation.md) |  | 

## Example

```python
from winthrop_client_python.models.ctb_volunteer_compensation_apply_input import CtbVolunteerCompensationApplyInput

# TODO update the JSON string below
json = "{}"
# create an instance of CtbVolunteerCompensationApplyInput from a JSON string
ctb_volunteer_compensation_apply_input_instance = CtbVolunteerCompensationApplyInput.from_json(json)
# print the JSON string representation of the object
print(CtbVolunteerCompensationApplyInput.to_json())

# convert the object into a dict
ctb_volunteer_compensation_apply_input_dict = ctb_volunteer_compensation_apply_input_instance.to_dict()
# create an instance of CtbVolunteerCompensationApplyInput from a dict
ctb_volunteer_compensation_apply_input_from_dict = CtbVolunteerCompensationApplyInput.from_dict(ctb_volunteer_compensation_apply_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


