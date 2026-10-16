# AdminRiNoteInputRiNoteQuickActions

Compensation-only \"Coach Quick Actions\" panel — only applied when the requested item's requestable_type is Compensation and both role and actions are present.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**actions** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_ri_note_input_ri_note_quick_actions import AdminRiNoteInputRiNoteQuickActions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRiNoteInputRiNoteQuickActions from a JSON string
admin_ri_note_input_ri_note_quick_actions_instance = AdminRiNoteInputRiNoteQuickActions.from_json(json)
# print the JSON string representation of the object
print(AdminRiNoteInputRiNoteQuickActions.to_json())

# convert the object into a dict
admin_ri_note_input_ri_note_quick_actions_dict = admin_ri_note_input_ri_note_quick_actions_instance.to_dict()
# create an instance of AdminRiNoteInputRiNoteQuickActions from a dict
admin_ri_note_input_ri_note_quick_actions_from_dict = AdminRiNoteInputRiNoteQuickActions.from_dict(admin_ri_note_input_ri_note_quick_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


