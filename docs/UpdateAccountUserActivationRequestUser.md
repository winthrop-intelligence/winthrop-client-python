# UpdateAccountUserActivationRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 
**password_confirmation** | **str** |  | 

## Example

```python
from winthrop_client_python.models.update_account_user_activation_request_user import UpdateAccountUserActivationRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountUserActivationRequestUser from a JSON string
update_account_user_activation_request_user_instance = UpdateAccountUserActivationRequestUser.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountUserActivationRequestUser.to_json())

# convert the object into a dict
update_account_user_activation_request_user_dict = update_account_user_activation_request_user_instance.to_dict()
# create an instance of UpdateAccountUserActivationRequestUser from a dict
update_account_user_activation_request_user_from_dict = UpdateAccountUserActivationRequestUser.from_dict(update_account_user_activation_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


