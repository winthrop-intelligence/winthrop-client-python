# RequestedItemNoteInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ri_note** | [**RequestedItemNoteInputRiNote**](RequestedItemNoteInputRiNote.md) |  | 

## Example

```python
from winthrop_client_python.models.requested_item_note_input import RequestedItemNoteInput

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemNoteInput from a JSON string
requested_item_note_input_instance = RequestedItemNoteInput.from_json(json)
# print the JSON string representation of the object
print(RequestedItemNoteInput.to_json())

# convert the object into a dict
requested_item_note_input_dict = requested_item_note_input_instance.to_dict()
# create an instance of RequestedItemNoteInput from a dict
requested_item_note_input_from_dict = RequestedItemNoteInput.from_dict(requested_item_note_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


