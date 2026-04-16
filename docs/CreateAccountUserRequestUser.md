# CreateAccountUserRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**title** | **str** |  | [optional] 
**email** | **str** | Email prefix only (before the @). The account email domain is appended automatically. | 
**time_zone** | **str** |  | [optional] 
**role_symbols** | **List[str]** |  | [optional] 
**schedule_sport_ids** | **List[int]** |  | [optional] 
**permissible_sport_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_account_user_request_user import CreateAccountUserRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccountUserRequestUser from a JSON string
create_account_user_request_user_instance = CreateAccountUserRequestUser.from_json(json)
# print the JSON string representation of the object
print(CreateAccountUserRequestUser.to_json())

# convert the object into a dict
create_account_user_request_user_dict = create_account_user_request_user_instance.to_dict()
# create an instance of CreateAccountUserRequestUser from a dict
create_account_user_request_user_from_dict = CreateAccountUserRequestUser.from_dict(create_account_user_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


