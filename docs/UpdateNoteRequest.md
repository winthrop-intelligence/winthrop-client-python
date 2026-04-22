# UpdateNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The updated note text | 

## Example

```python
from winthrop_client_python.models.update_note_request import UpdateNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNoteRequest from a JSON string
update_note_request_instance = UpdateNoteRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateNoteRequest.to_json())

# convert the object into a dict
update_note_request_dict = update_note_request_instance.to_dict()
# create an instance of UpdateNoteRequest from a dict
update_note_request_from_dict = UpdateNoteRequest.from_dict(update_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


