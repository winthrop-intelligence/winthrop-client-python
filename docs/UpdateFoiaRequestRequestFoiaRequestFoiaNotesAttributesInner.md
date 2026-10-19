# UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**destroy** | **bool** | Delete the identified note from this request. | [optional] 

## Example

```python
from winthrop_client_python.models.update_foia_request_request_foia_request_foia_notes_attributes_inner import UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner from a JSON string
update_foia_request_request_foia_request_foia_notes_attributes_inner_instance = UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner.from_json(json)
# print the JSON string representation of the object
print(UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner.to_json())

# convert the object into a dict
update_foia_request_request_foia_request_foia_notes_attributes_inner_dict = update_foia_request_request_foia_request_foia_notes_attributes_inner_instance.to_dict()
# create an instance of UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner from a dict
update_foia_request_request_foia_request_foia_notes_attributes_inner_from_dict = UpdateFoiaRequestRequestFoiaRequestFoiaNotesAttributesInner.from_dict(update_foia_request_request_foia_request_foia_notes_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


