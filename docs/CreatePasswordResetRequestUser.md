# CreatePasswordResetRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address of the account to reset | 

## Example

```python
from winthrop_client_python.models.create_password_reset_request_user import CreatePasswordResetRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasswordResetRequestUser from a JSON string
create_password_reset_request_user_instance = CreatePasswordResetRequestUser.from_json(json)
# print the JSON string representation of the object
print(CreatePasswordResetRequestUser.to_json())

# convert the object into a dict
create_password_reset_request_user_dict = create_password_reset_request_user_instance.to_dict()
# create an instance of CreatePasswordResetRequestUser from a dict
create_password_reset_request_user_from_dict = CreatePasswordResetRequestUser.from_dict(create_password_reset_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


