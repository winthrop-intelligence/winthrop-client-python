# AdminYoutubeVideoListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**filter_options** | [**AdminYoutubeVideoListMetaAllOfFilterOptions**](AdminYoutubeVideoListMetaAllOfFilterOptions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_youtube_video_list_meta import AdminYoutubeVideoListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminYoutubeVideoListMeta from a JSON string
admin_youtube_video_list_meta_instance = AdminYoutubeVideoListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminYoutubeVideoListMeta.to_json())

# convert the object into a dict
admin_youtube_video_list_meta_dict = admin_youtube_video_list_meta_instance.to_dict()
# create an instance of AdminYoutubeVideoListMeta from a dict
admin_youtube_video_list_meta_from_dict = AdminYoutubeVideoListMeta.from_dict(admin_youtube_video_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


