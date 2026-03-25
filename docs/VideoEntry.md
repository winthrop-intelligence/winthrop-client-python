# VideoEntry


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
from winthrop_client_python.models.video_entry import VideoEntry

# TODO update the JSON string below
json = "{}"
# create an instance of VideoEntry from a JSON string
video_entry_instance = VideoEntry.from_json(json)
# print the JSON string representation of the object
print(VideoEntry.to_json())

# convert the object into a dict
video_entry_dict = video_entry_instance.to_dict()
# create an instance of VideoEntry from a dict
video_entry_from_dict = VideoEntry.from_dict(video_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


