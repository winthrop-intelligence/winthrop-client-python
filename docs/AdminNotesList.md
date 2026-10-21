# AdminNotesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminNotesListMeta**](AdminNotesListMeta.md) |  | [optional] 
**data** | [**List[AdminNote]**](AdminNote.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_notes_list import AdminNotesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNotesList from a JSON string
admin_notes_list_instance = AdminNotesList.from_json(json)
# print the JSON string representation of the object
print(AdminNotesList.to_json())

# convert the object into a dict
admin_notes_list_dict = admin_notes_list_instance.to_dict()
# create an instance of AdminNotesList from a dict
admin_notes_list_from_dict = AdminNotesList.from_dict(admin_notes_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


