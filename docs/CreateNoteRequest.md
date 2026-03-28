# CreateNoteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notable_type** | **str** | The model type (e.g. \&quot;Coach\&quot;) | 
**notable_id** | **int** | The ID of the notable record | 
**content** | **str** | The note text | 

## Example

```python
from winthrop_client_python.models.create_note_request import CreateNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNoteRequest from a JSON string
create_note_request_instance = CreateNoteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateNoteRequest.to_json())

# convert the object into a dict
create_note_request_dict = create_note_request_instance.to_dict()
# create an instance of CreateNoteRequest from a dict
create_note_request_from_dict = CreateNoteRequest.from_dict(create_note_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


