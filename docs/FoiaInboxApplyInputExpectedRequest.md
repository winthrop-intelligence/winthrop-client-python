# FoiaInboxApplyInputExpectedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by_school** | **date** |  | 
**updated_by_wi** | **date** |  | 
**foia_notes_sha256** | **str** |  | 

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


