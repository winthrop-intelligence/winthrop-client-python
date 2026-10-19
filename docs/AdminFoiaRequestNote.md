# AdminFoiaRequestNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**content** | **str** |  | 
**author** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.admin_foia_request_note import AdminFoiaRequestNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestNote from a JSON string
admin_foia_request_note_instance = AdminFoiaRequestNote.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestNote.to_json())

# convert the object into a dict
admin_foia_request_note_dict = admin_foia_request_note_instance.to_dict()
# create an instance of AdminFoiaRequestNote from a dict
admin_foia_request_note_from_dict = AdminFoiaRequestNote.from_dict(admin_foia_request_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


