# CtbCompensationApplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctb_compensation_apply** | [**CtbCompensationApplyInput**](CtbCompensationApplyInput.md) |  | 

## Example

```python
from winthrop_client_python.models.ctb_compensation_apply_request import CtbCompensationApplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CtbCompensationApplyRequest from a JSON string
ctb_compensation_apply_request_instance = CtbCompensationApplyRequest.from_json(json)
# print the JSON string representation of the object
print(CtbCompensationApplyRequest.to_json())

# convert the object into a dict
ctb_compensation_apply_request_dict = ctb_compensation_apply_request_instance.to_dict()
# create an instance of CtbCompensationApplyRequest from a dict
ctb_compensation_apply_request_from_dict = CtbCompensationApplyRequest.from_dict(ctb_compensation_apply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


