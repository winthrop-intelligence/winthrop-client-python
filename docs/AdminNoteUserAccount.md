# AdminNoteUserAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**subscription_type_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_note_user_account import AdminNoteUserAccount

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNoteUserAccount from a JSON string
admin_note_user_account_instance = AdminNoteUserAccount.from_json(json)
# print the JSON string representation of the object
print(AdminNoteUserAccount.to_json())

# convert the object into a dict
admin_note_user_account_dict = admin_note_user_account_instance.to_dict()
# create an instance of AdminNoteUserAccount from a dict
admin_note_user_account_from_dict = AdminNoteUserAccount.from_dict(admin_note_user_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


