# CoachVideoEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**youtube_id** | **str** |  | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**published_at** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_video_entry import CoachVideoEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CoachVideoEntry from a JSON string
coach_video_entry_instance = CoachVideoEntry.from_json(json)
# print the JSON string representation of the object
print(CoachVideoEntry.to_json())

# convert the object into a dict
coach_video_entry_dict = coach_video_entry_instance.to_dict()
# create an instance of CoachVideoEntry from a dict
coach_video_entry_from_dict = CoachVideoEntry.from_dict(coach_video_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


