# UpdateAdminNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | [**UpdateAdminNoteRequestNote**](UpdateAdminNoteRequestNote.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_note_request import UpdateAdminNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminNoteRequest from a JSON string
update_admin_note_request_instance = UpdateAdminNoteRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminNoteRequest.to_json())

# convert the object into a dict
update_admin_note_request_dict = update_admin_note_request_instance.to_dict()
# create an instance of UpdateAdminNoteRequest from a dict
update_admin_note_request_from_dict = UpdateAdminNoteRequest.from_dict(update_admin_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


