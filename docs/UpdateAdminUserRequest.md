# UpdateAdminUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UpdateAdminUserRequestUser**](UpdateAdminUserRequestUser.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_user_request import UpdateAdminUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminUserRequest from a JSON string
update_admin_user_request_instance = UpdateAdminUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminUserRequest.to_json())

# convert the object into a dict
update_admin_user_request_dict = update_admin_user_request_instance.to_dict()
# create an instance of UpdateAdminUserRequest from a dict
update_admin_user_request_from_dict = UpdateAdminUserRequest.from_dict(update_admin_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


