# FoiaFollowUpNote


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
from winthrop_client_python.models.foia_follow_up_note import FoiaFollowUpNote

# TODO update the JSON string below
json = "{}"
# create an instance of FoiaFollowUpNote from a JSON string
foia_follow_up_note_instance = FoiaFollowUpNote.from_json(json)
# print the JSON string representation of the object
print(FoiaFollowUpNote.to_json())

# convert the object into a dict
foia_follow_up_note_dict = foia_follow_up_note_instance.to_dict()
# create an instance of FoiaFollowUpNote from a dict
foia_follow_up_note_from_dict = FoiaFollowUpNote.from_dict(foia_follow_up_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


