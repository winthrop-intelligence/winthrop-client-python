# FoiaInboxApplyResponseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request** | [**FoiaInboxApplyResponseResultFoiaRequest**](FoiaInboxApplyResponseResultFoiaRequest.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_apply_response_result import FoiaInboxApplyResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxApplyResponseResult from a JSON string
foia_inbox_apply_response_result_instance = FoiaInboxApplyResponseResult.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxApplyResponseResult.to_json())

# convert the object into a dict
foia_inbox_apply_response_result_dict = foia_inbox_apply_response_result_instance.to_dict()
# create an instance of FoiaInboxApplyResponseResult from a dict
foia_inbox_apply_response_result_from_dict = FoiaInboxApplyResponseResult.from_dict(foia_inbox_apply_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


