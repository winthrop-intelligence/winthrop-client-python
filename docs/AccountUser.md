# AccountUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**is_account_admin** | **bool** |  | [optional] 
**abilities** | **List[str]** |  | [optional] 
**schedule_sports** | **List[str]** |  | [optional] 
**permissible_sports** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.account_user import AccountUser

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUser from a JSON string
account_user_instance = AccountUser.from_json(json)
# print the JSON string representation of the object
print(AccountUser.to_json())

# convert the object into a dict
account_user_dict = account_user_instance.to_dict()
# create an instance of AccountUser from a dict
account_user_from_dict = AccountUser.from_dict(account_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


