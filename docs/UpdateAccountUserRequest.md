# UpdateAccountUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UpdateAccountUserRequestUser**](UpdateAccountUserRequestUser.md) |  | 

## Example

```python
from winthrop_client_python.models.update_account_user_request import UpdateAccountUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountUserRequest from a JSON string
update_account_user_request_instance = UpdateAccountUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountUserRequest.to_json())

# convert the object into a dict
update_account_user_request_dict = update_account_user_request_instance.to_dict()
# create an instance of UpdateAccountUserRequest from a dict
update_account_user_request_from_dict = UpdateAccountUserRequest.from_dict(update_account_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


