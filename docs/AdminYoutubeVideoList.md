# AdminYoutubeVideoList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminYoutubeVideo]**](AdminYoutubeVideo.md) |  | [optional] 
**meta** | [**AdminYoutubeVideoListMeta**](AdminYoutubeVideoListMeta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_youtube_video_list import AdminYoutubeVideoList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminYoutubeVideoList from a JSON string
admin_youtube_video_list_instance = AdminYoutubeVideoList.from_json(json)
# print the JSON string representation of the object
print(AdminYoutubeVideoList.to_json())

# convert the object into a dict
admin_youtube_video_list_dict = admin_youtube_video_list_instance.to_dict()
# create an instance of AdminYoutubeVideoList from a dict
admin_youtube_video_list_from_dict = AdminYoutubeVideoList.from_dict(admin_youtube_video_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


