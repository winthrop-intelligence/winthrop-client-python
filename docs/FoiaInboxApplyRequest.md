# FoiaInboxApplyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_inbox_apply** | [**FoiaInboxApplyInput**](FoiaInboxApplyInput.md) |  | 

## Example

```python
from winthrop_client_python.models.foia_inbox_apply_request import FoiaInboxApplyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxApplyRequest from a JSON string
foia_inbox_apply_request_instance = FoiaInboxApplyRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxApplyRequest.to_json())

# convert the object into a dict
foia_inbox_apply_request_dict = foia_inbox_apply_request_instance.to_dict()
# create an instance of FoiaInboxApplyRequest from a dict
foia_inbox_apply_request_from_dict = FoiaInboxApplyRequest.from_dict(foia_inbox_apply_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


