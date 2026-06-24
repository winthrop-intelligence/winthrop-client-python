# RequestedItemNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RequestedItemNote**](RequestedItemNote.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.requested_item_note_response import RequestedItemNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemNoteResponse from a JSON string
requested_item_note_response_instance = RequestedItemNoteResponse.from_json(json)
# print the JSON string representation of the object
print(RequestedItemNoteResponse.to_json())

# convert the object into a dict
requested_item_note_response_dict = requested_item_note_response_instance.to_dict()
# create an instance of RequestedItemNoteResponse from a dict
requested_item_note_response_from_dict = RequestedItemNoteResponse.from_dict(requested_item_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


