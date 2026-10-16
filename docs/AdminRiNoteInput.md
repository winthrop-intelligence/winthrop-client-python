# AdminRiNoteInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ri_note** | [**AdminRiNoteInputRiNote**](AdminRiNoteInputRiNote.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_ri_note_input import AdminRiNoteInput

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRiNoteInput from a JSON string
admin_ri_note_input_instance = AdminRiNoteInput.from_json(json)
# print the JSON string representation of the object
print(AdminRiNoteInput.to_json())

# convert the object into a dict
admin_ri_note_input_dict = admin_ri_note_input_instance.to_dict()
# create an instance of AdminRiNoteInput from a dict
admin_ri_note_input_from_dict = AdminRiNoteInput.from_dict(admin_ri_note_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


