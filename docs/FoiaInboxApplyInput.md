# FoiaInboxApplyInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox** | **str** |  | 
**gmail_message_id** | **str** |  | 
**gmail_thread_id** | **str** |  | 
**run_id** | **str** |  | 
**foia_request_id** | **int** |  | 
**school_id** | **int** |  | 
**decision_sha256** | **str** |  | 
**expected_request** | [**FoiaInboxApplyInputExpectedRequest**](FoiaInboxApplyInputExpectedRequest.md) |  | 
**effects** | [**FoiaInboxEffects**](FoiaInboxEffects.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_apply_input import FoiaInboxApplyInput

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxApplyInput from a JSON string
foia_inbox_apply_input_instance = FoiaInboxApplyInput.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxApplyInput.to_json())

# convert the object into a dict
foia_inbox_apply_input_dict = foia_inbox_apply_input_instance.to_dict()
# create an instance of FoiaInboxApplyInput from a dict
foia_inbox_apply_input_from_dict = FoiaInboxApplyInput.from_dict(foia_inbox_apply_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


