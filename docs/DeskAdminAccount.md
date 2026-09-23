# DeskAdminAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_account import DeskAdminAccount

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminAccount from a JSON string
desk_admin_account_instance = DeskAdminAccount.from_json(json)
# print the JSON string representation of the object
print(DeskAdminAccount.to_json())

# convert the object into a dict
desk_admin_account_dict = desk_admin_account_instance.to_dict()
# create an instance of DeskAdminAccount from a dict
desk_admin_account_from_dict = DeskAdminAccount.from_dict(desk_admin_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


