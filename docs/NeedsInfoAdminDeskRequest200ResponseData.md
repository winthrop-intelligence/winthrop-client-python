# NeedsInfoAdminDeskRequest200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**status** | **str** |  | 
**admin_note** | **str** |  | 
**clock_paused** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.needs_info_admin_desk_request200_response_data import NeedsInfoAdminDeskRequest200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of NeedsInfoAdminDeskRequest200ResponseData from a JSON string
needs_info_admin_desk_request200_response_data_instance = NeedsInfoAdminDeskRequest200ResponseData.from_json(json)
# print the JSON string representation of the object
print(NeedsInfoAdminDeskRequest200ResponseData.to_json())

# convert the object into a dict
needs_info_admin_desk_request200_response_data_dict = needs_info_admin_desk_request200_response_data_instance.to_dict()
# create an instance of NeedsInfoAdminDeskRequest200ResponseData from a dict
needs_info_admin_desk_request200_response_data_from_dict = NeedsInfoAdminDeskRequest200ResponseData.from_dict(needs_info_admin_desk_request200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


