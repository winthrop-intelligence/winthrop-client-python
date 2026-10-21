# AdminNoteNotable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_note_notable import AdminNoteNotable

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNoteNotable from a JSON string
admin_note_notable_instance = AdminNoteNotable.from_json(json)
# print the JSON string representation of the object
print(AdminNoteNotable.to_json())

# convert the object into a dict
admin_note_notable_dict = admin_note_notable_instance.to_dict()
# create an instance of AdminNoteNotable from a dict
admin_note_notable_from_dict = AdminNoteNotable.from_dict(admin_note_notable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


