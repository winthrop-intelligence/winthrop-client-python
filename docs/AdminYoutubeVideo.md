# AdminYoutubeVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**youtube_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**published_at** | **datetime** |  | [optional] 
**state** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**link** | **str** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**coach** | [**AdminYoutubeVideoCoach**](AdminYoutubeVideoCoach.md) |  | [optional] 
**school** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 
**sport** | [**CompensationComparisonResolvedScopeConference**](CompensationComparisonResolvedScopeConference.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_youtube_video import AdminYoutubeVideo

# TODO update the JSON string below
json = "{}"
# create an instance of AdminYoutubeVideo from a JSON string
admin_youtube_video_instance = AdminYoutubeVideo.from_json(json)
# print the JSON string representation of the object
print(AdminYoutubeVideo.to_json())

# convert the object into a dict
admin_youtube_video_dict = admin_youtube_video_instance.to_dict()
# create an instance of AdminYoutubeVideo from a dict
admin_youtube_video_from_dict = AdminYoutubeVideo.from_dict(admin_youtube_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


