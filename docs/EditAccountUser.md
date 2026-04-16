# EditAccountUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**role_symbols** | **List[str]** |  | [optional] 
**schedule_sport_ids** | **List[int]** |  | [optional] 
**permissible_sport_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.edit_account_user import EditAccountUser

# TODO update the JSON string below
json = "{}"
# create an instance of EditAccountUser from a JSON string
edit_account_user_instance = EditAccountUser.from_json(json)
# print the JSON string representation of the object
print(EditAccountUser.to_json())

# convert the object into a dict
edit_account_user_dict = edit_account_user_instance.to_dict()
# create an instance of EditAccountUser from a dict
edit_account_user_from_dict = EditAccountUser.from_dict(edit_account_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


