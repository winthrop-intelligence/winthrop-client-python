# AdminNoteUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**account** | [**AdminNoteUserAccount**](AdminNoteUserAccount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_note_user import AdminNoteUser

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNoteUser from a JSON string
admin_note_user_instance = AdminNoteUser.from_json(json)
# print the JSON string representation of the object
print(AdminNoteUser.to_json())

# convert the object into a dict
admin_note_user_dict = admin_note_user_instance.to_dict()
# create an instance of AdminNoteUser from a dict
admin_note_user_from_dict = AdminNoteUser.from_dict(admin_note_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


