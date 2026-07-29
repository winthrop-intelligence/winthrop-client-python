# FoiaInboxNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user_id** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.foia_inbox_note import FoiaInboxNote

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaInboxNote from a JSON string
foia_inbox_note_instance = FoiaInboxNote.from_json(json)
# print the JSON string representation of the object
print(FoiaInboxNote.to_json())

# convert the object into a dict
foia_inbox_note_dict = foia_inbox_note_instance.to_dict()
# create an instance of FoiaInboxNote from a dict
foia_inbox_note_from_dict = FoiaInboxNote.from_dict(foia_inbox_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


