# AdminYoutubeVideoCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_youtube_video_coach import AdminYoutubeVideoCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AdminYoutubeVideoCoach from a JSON string
admin_youtube_video_coach_instance = AdminYoutubeVideoCoach.from_json(json)
# print the JSON string representation of the object
print(AdminYoutubeVideoCoach.to_json())

# convert the object into a dict
admin_youtube_video_coach_dict = admin_youtube_video_coach_instance.to_dict()
# create an instance of AdminYoutubeVideoCoach from a dict
admin_youtube_video_coach_from_dict = AdminYoutubeVideoCoach.from_dict(admin_youtube_video_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


