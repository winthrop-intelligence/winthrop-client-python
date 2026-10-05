# GetAdminDeskRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskAdminQueueRow**](DeskAdminQueueRow.md) |  | 

## Example

```python
from winthrop_client_python.models.get_admin_desk_request200_response import GetAdminDeskRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdminDeskRequest200Response from a JSON string
get_admin_desk_request200_response_instance = GetAdminDeskRequest200Response.from_json(json)
# print the JSON string representation of the object
print(GetAdminDeskRequest200Response.to_json())

# convert the object into a dict
get_admin_desk_request200_response_dict = get_admin_desk_request200_response_instance.to_dict()
# create an instance of GetAdminDeskRequest200Response from a dict
get_admin_desk_request200_response_from_dict = GetAdminDeskRequest200Response.from_dict(get_admin_desk_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


