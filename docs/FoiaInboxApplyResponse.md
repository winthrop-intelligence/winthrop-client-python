# FoiaInboxApplyResponse


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
**request_sha256** | **str** |  | 
**status** | **str** |  | 
**foia_contact_results** | [**List[FoiaInboxContactResult]**](FoiaInboxContactResult.md) | Typed authoritative read-back for selected FOIA-contact effects; empty when none were selected. | [optional] 
**result** | **Dict[str, object]** |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_apply_response import FoiaInboxApplyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxApplyResponse from a JSON string
foia_inbox_apply_response_instance = FoiaInboxApplyResponse.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxApplyResponse.to_json())

# convert the object into a dict
foia_inbox_apply_response_dict = foia_inbox_apply_response_instance.to_dict()
# create an instance of FoiaInboxApplyResponse from a dict
foia_inbox_apply_response_from_dict = FoiaInboxApplyResponse.from_dict(foia_inbox_apply_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


