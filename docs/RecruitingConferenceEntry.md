# RecruitingConferenceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | **str** |  | 
**school_id** | **int** |  | 
**class_rank** | **int** |  | [optional] 
**conference_record** | **str** |  | [optional] 
**overall_record** | **str** |  | [optional] 
**postseason** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.recruiting_conference_entry import RecruitingConferenceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RecruitingConferenceEntry from a JSON string
recruiting_conference_entry_instance = RecruitingConferenceEntry.from_json(json)
# print the JSON string representation of the object
print(RecruitingConferenceEntry.to_json())

# convert the object into a dict
recruiting_conference_entry_dict = recruiting_conference_entry_instance.to_dict()
# create an instance of RecruitingConferenceEntry from a dict
recruiting_conference_entry_from_dict = RecruitingConferenceEntry.from_dict(recruiting_conference_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


