# CreateYoutubeVideoRequestYoutubeVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**youtube_id** | **str** |  | 
**title** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**coach_id** | **int** |  | 
**school_id** | **int** |  | 

## Example

```python
from winthrop_client_python.models.create_youtube_video_request_youtube_video import CreateYoutubeVideoRequestYoutubeVideo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateYoutubeVideoRequestYoutubeVideo from a JSON string
create_youtube_video_request_youtube_video_instance = CreateYoutubeVideoRequestYoutubeVideo.from_json(json)
# print the JSON string representation of the object
print(CreateYoutubeVideoRequestYoutubeVideo.to_json())

# convert the object into a dict
create_youtube_video_request_youtube_video_dict = create_youtube_video_request_youtube_video_instance.to_dict()
# create an instance of CreateYoutubeVideoRequestYoutubeVideo from a dict
create_youtube_video_request_youtube_video_from_dict = CreateYoutubeVideoRequestYoutubeVideo.from_dict(create_youtube_video_request_youtube_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


