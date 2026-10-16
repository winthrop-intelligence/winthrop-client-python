# AdminYoutubeVideoListMetaAllOfFilterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | [**List[AdminYoutubeVideoListMetaAllOfFilterOptionsStatesInner]**](AdminYoutubeVideoListMetaAllOfFilterOptionsStatesInner.md) |  | [optional] 
**sports** | [**List[IdName]**](IdName.md) |  | [optional] 
**conferences** | [**List[IdName]**](IdName.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_youtube_video_list_meta_all_of_filter_options import AdminYoutubeVideoListMetaAllOfFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminYoutubeVideoListMetaAllOfFilterOptions from a JSON string
admin_youtube_video_list_meta_all_of_filter_options_instance = AdminYoutubeVideoListMetaAllOfFilterOptions.from_json(json)
# print the JSON string representation of the object
print(AdminYoutubeVideoListMetaAllOfFilterOptions.to_json())

# convert the object into a dict
admin_youtube_video_list_meta_all_of_filter_options_dict = admin_youtube_video_list_meta_all_of_filter_options_instance.to_dict()
# create an instance of AdminYoutubeVideoListMetaAllOfFilterOptions from a dict
admin_youtube_video_list_meta_all_of_filter_options_from_dict = AdminYoutubeVideoListMetaAllOfFilterOptions.from_dict(admin_youtube_video_list_meta_all_of_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


