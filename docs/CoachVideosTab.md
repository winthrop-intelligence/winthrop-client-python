# CoachVideosTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_see_videos** | **bool** |  | 
**videos** | [**List[VideoEntry]**](VideoEntry.md) |  | 

## Example

```python
from winthrop_client_python.models.coach_videos_tab import CoachVideosTab

# TODO update the JSON string below
json = "{}"
# create an instance of CoachVideosTab from a JSON string
coach_videos_tab_instance = CoachVideosTab.from_json(json)
# print the JSON string representation of the object
print(CoachVideosTab.to_json())

# convert the object into a dict
coach_videos_tab_dict = coach_videos_tab_instance.to_dict()
# create an instance of CoachVideosTab from a dict
coach_videos_tab_from_dict = CoachVideosTab.from_dict(coach_videos_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


