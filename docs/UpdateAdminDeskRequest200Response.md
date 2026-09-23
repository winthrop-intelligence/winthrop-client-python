# UpdateAdminDeskRequest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateAdminDeskRequest200ResponseData**](UpdateAdminDeskRequest200ResponseData.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_desk_request200_response import UpdateAdminDeskRequest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminDeskRequest200Response from a JSON string
update_admin_desk_request200_response_instance = UpdateAdminDeskRequest200Response.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminDeskRequest200Response.to_json())

# convert the object into a dict
update_admin_desk_request200_response_dict = update_admin_desk_request200_response_instance.to_dict()
# create an instance of UpdateAdminDeskRequest200Response from a dict
update_admin_desk_request200_response_from_dict = UpdateAdminDeskRequest200Response.from_dict(update_admin_desk_request200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


