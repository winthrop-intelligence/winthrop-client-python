# RequestedItemNoteInputRiNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Note text to create or append. Leading and trailing whitespace is trimmed; blank or whitespace-only values are rejected. | 

## Example

```python
from winthrop_client_python.models.requested_item_note_input_ri_note import RequestedItemNoteInputRiNote

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemNoteInputRiNote from a JSON string
requested_item_note_input_ri_note_instance = RequestedItemNoteInputRiNote.from_json(json)
# print the JSON string representation of the object
print(RequestedItemNoteInputRiNote.to_json())

# convert the object into a dict
requested_item_note_input_ri_note_dict = requested_item_note_input_ri_note_instance.to_dict()
# create an instance of RequestedItemNoteInputRiNote from a dict
requested_item_note_input_ri_note_from_dict = RequestedItemNoteInputRiNote.from_dict(requested_item_note_input_ri_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


