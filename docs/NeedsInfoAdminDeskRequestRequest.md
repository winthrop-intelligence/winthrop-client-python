# NeedsInfoAdminDeskRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**follow_up_subject** | **str** |  | 
**follow_up_body** | **str** |  | 
**client_note** | **str** | What the customer&#39;s pending card shows; defaults to the follow-up body | [optional] 

## Example

```python
from winthrop_client_python.models.needs_info_admin_desk_request_request import NeedsInfoAdminDeskRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NeedsInfoAdminDeskRequestRequest from a JSON string
needs_info_admin_desk_request_request_instance = NeedsInfoAdminDeskRequestRequest.from_json(json)
# print the JSON string representation of the object
print(NeedsInfoAdminDeskRequestRequest.to_json())

# convert the object into a dict
needs_info_admin_desk_request_request_dict = needs_info_admin_desk_request_request_instance.to_dict()
# create an instance of NeedsInfoAdminDeskRequestRequest from a dict
needs_info_admin_desk_request_request_from_dict = NeedsInfoAdminDeskRequestRequest.from_dict(needs_info_admin_desk_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


