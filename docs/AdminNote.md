# AdminNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**notable_id** | **int** |  | [optional] 
**notable_type** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**AdminNoteUser**](AdminNoteUser.md) |  | [optional] 
**notable** | [**AdminNoteNotable**](AdminNoteNotable.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_note import AdminNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNote from a JSON string
admin_note_instance = AdminNote.from_json(json)
# print the JSON string representation of the object
print(AdminNote.to_json())

# convert the object into a dict
admin_note_dict = admin_note_instance.to_dict()
# create an instance of AdminNote from a dict
admin_note_from_dict = AdminNote.from_dict(admin_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


