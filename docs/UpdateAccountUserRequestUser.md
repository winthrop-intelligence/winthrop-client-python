# UpdateAccountUserRequestUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_symbols** | **List[str]** |  | 
**schedule_sport_ids** | **List[int]** |  | [optional] 
**permissible_sport_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_account_user_request_user import UpdateAccountUserRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccountUserRequestUser from a JSON string
update_account_user_request_user_instance = UpdateAccountUserRequestUser.from_json(json)
# print the JSON string representation of the object
print(UpdateAccountUserRequestUser.to_json())

# convert the object into a dict
update_account_user_request_user_dict = update_account_user_request_user_instance.to_dict()
# create an instance of UpdateAccountUserRequestUser from a dict
update_account_user_request_user_from_dict = UpdateAccountUserRequestUser.from_dict(update_account_user_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


