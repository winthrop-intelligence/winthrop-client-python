# UpdateAccountUserActivationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmation_token** | **str** | The confirmation token from the invitation email | 
**user** | [**UpdateAccountUserActivationRequestUser**](UpdateAccountUserActivationRequestUser.md) |  | 

## Example

```python
from winthrop_client_python.models.update_account_user_activation_request import UpdateAccountUserActivationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountUserActivationRequest from a JSON string
update_account_user_activation_request_instance = UpdateAccountUserActivationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountUserActivationRequest.to_json())

# convert the object into a dict
update_account_user_activation_request_dict = update_account_user_activation_request_instance.to_dict()
# create an instance of UpdateAccountUserActivationRequest from a dict
update_account_user_activation_request_from_dict = UpdateAccountUserActivationRequest.from_dict(update_account_user_activation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


