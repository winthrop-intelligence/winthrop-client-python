# FoiaInboxApplyResponseResultFoiaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**follow_up_date** | **date** |  | [optional] 
**follow_up_date_explicit** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_apply_response_result_foia_request import FoiaInboxApplyResponseResultFoiaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxApplyResponseResultFoiaRequest from a JSON string
foia_inbox_apply_response_result_foia_request_instance = FoiaInboxApplyResponseResultFoiaRequest.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxApplyResponseResultFoiaRequest.to_json())

# convert the object into a dict
foia_inbox_apply_response_result_foia_request_dict = foia_inbox_apply_response_result_foia_request_instance.to_dict()
# create an instance of FoiaInboxApplyResponseResultFoiaRequest from a dict
foia_inbox_apply_response_result_foia_request_from_dict = FoiaInboxApplyResponseResultFoiaRequest.from_dict(foia_inbox_apply_response_result_foia_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


