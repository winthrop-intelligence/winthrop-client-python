# CreateAdminUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**CreateAdminUserRequestUser**](CreateAdminUserRequestUser.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_user_request import CreateAdminUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminUserRequest from a JSON string
create_admin_user_request_instance = CreateAdminUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminUserRequest.to_json())

# convert the object into a dict
create_admin_user_request_dict = create_admin_user_request_instance.to_dict()
# create an instance of CreateAdminUserRequest from a dict
create_admin_user_request_from_dict = CreateAdminUserRequest.from_dict(create_admin_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


