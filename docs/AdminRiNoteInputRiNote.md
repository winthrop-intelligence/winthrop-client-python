# AdminRiNoteInputRiNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** |  | [optional] 
**user_id** | **int** | Author of the note. Defaults to the current admin user when omitted. | [optional] 
**quick_actions** | [**AdminRiNoteInputRiNoteQuickActions**](AdminRiNoteInputRiNoteQuickActions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_ri_note_input_ri_note import AdminRiNoteInputRiNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRiNoteInputRiNote from a JSON string
admin_ri_note_input_ri_note_instance = AdminRiNoteInputRiNote.from_json(json)
# print the JSON string representation of the object
print(AdminRiNoteInputRiNote.to_json())

# convert the object into a dict
admin_ri_note_input_ri_note_dict = admin_ri_note_input_ri_note_instance.to_dict()
# create an instance of AdminRiNoteInputRiNote from a dict
admin_ri_note_input_ri_note_from_dict = AdminRiNoteInputRiNote.from_dict(admin_ri_note_input_ri_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


