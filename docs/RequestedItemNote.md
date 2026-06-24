# RequestedItemNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**requested_item_id** | **int** |  | 
**note** | **str** |  | 
**user_id** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.requested_item_note import RequestedItemNote

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedItemNote from a JSON string
requested_item_note_instance = RequestedItemNote.from_json(json)
# print the JSON string representation of the object
print(RequestedItemNote.to_json())

# convert the object into a dict
requested_item_note_dict = requested_item_note_instance.to_dict()
# create an instance of RequestedItemNote from a dict
requested_item_note_from_dict = RequestedItemNote.from_dict(requested_item_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


