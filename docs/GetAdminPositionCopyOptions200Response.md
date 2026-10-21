# GetAdminPositionCopyOptions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**seasons** | [**List[GetAdminPositionCopyOptions200ResponseSeasonsInner]**](GetAdminPositionCopyOptions200ResponseSeasonsInner.md) |  | 

## Example

```python
from winthrop_client_python.models.get_admin_position_copy_options200_response import GetAdminPositionCopyOptions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdminPositionCopyOptions200Response from a JSON string
get_admin_position_copy_options200_response_instance = GetAdminPositionCopyOptions200Response.from_json(json)
# print the JSON string representation of the object
print(GetAdminPositionCopyOptions200Response.to_json())

# convert the object into a dict
get_admin_position_copy_options200_response_dict = get_admin_position_copy_options200_response_instance.to_dict()
# create an instance of GetAdminPositionCopyOptions200Response from a dict
get_admin_position_copy_options200_response_from_dict = GetAdminPositionCopyOptions200Response.from_dict(get_admin_position_copy_options200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


