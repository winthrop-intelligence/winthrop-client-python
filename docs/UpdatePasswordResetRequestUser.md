# UpdatePasswordResetRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reset_password_token** | **str** | The token from the password reset email | 
**password** | **str** | The new password | 
**password_confirmation** | **str** | Confirmation of the new password | 

## Example

```python
from winthrop_client_python.models.update_password_reset_request_user import UpdatePasswordResetRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordResetRequestUser from a JSON string
update_password_reset_request_user_instance = UpdatePasswordResetRequestUser.from_json(json)
# print the JSON string representation of the object
print(UpdatePasswordResetRequestUser.to_json())

# convert the object into a dict
update_password_reset_request_user_dict = update_password_reset_request_user_instance.to_dict()
# create an instance of UpdatePasswordResetRequestUser from a dict
update_password_reset_request_user_from_dict = UpdatePasswordResetRequestUser.from_dict(update_password_reset_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


