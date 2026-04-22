# EditAccountUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**EditAccountUser**](EditAccountUser.md) |  | [optional] 
**role_options** | [**List[RoleOption]**](RoleOption.md) |  | [optional] 
**schedulable_sports** | [**List[SportOption]**](SportOption.md) |  | [optional] 
**all_sports** | [**List[SportOption]**](SportOption.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.edit_account_user_response import EditAccountUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EditAccountUserResponse from a JSON string
edit_account_user_response_instance = EditAccountUserResponse.from_json(json)
# print the JSON string representation of the object
print(EditAccountUserResponse.to_json())

# convert the object into a dict
edit_account_user_response_dict = edit_account_user_response_instance.to_dict()
# create an instance of EditAccountUserResponse from a dict
edit_account_user_response_from_dict = EditAccountUserResponse.from_dict(edit_account_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


