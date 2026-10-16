# CreateYoutubeVideoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**youtube_video** | [**CreateYoutubeVideoRequestYoutubeVideo**](CreateYoutubeVideoRequestYoutubeVideo.md) |  | 

## Example

```python
from winthrop_client_python.models.create_youtube_video_request import CreateYoutubeVideoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateYoutubeVideoRequest from a JSON string
create_youtube_video_request_instance = CreateYoutubeVideoRequest.from_json(json)
# print the JSON string representation of the object
print(CreateYoutubeVideoRequest.to_json())

# convert the object into a dict
create_youtube_video_request_dict = create_youtube_video_request_instance.to_dict()
# create an instance of CreateYoutubeVideoRequest from a dict
create_youtube_video_request_from_dict = CreateYoutubeVideoRequest.from_dict(create_youtube_video_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


