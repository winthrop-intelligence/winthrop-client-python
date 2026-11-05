# AdminRankingsUploadInfoMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_headers** | **List[str]** |  | [optional] 
**optional_headers** | **List[str]** |  | [optional] 
**jobs** | **List[object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_rankings_upload_info_meta import AdminRankingsUploadInfoMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRankingsUploadInfoMeta from a JSON string
admin_rankings_upload_info_meta_instance = AdminRankingsUploadInfoMeta.from_json(json)
# print the JSON string representation of the object
print(AdminRankingsUploadInfoMeta.to_json())

# convert the object into a dict
admin_rankings_upload_info_meta_dict = admin_rankings_upload_info_meta_instance.to_dict()
# create an instance of AdminRankingsUploadInfoMeta from a dict
admin_rankings_upload_info_meta_from_dict = AdminRankingsUploadInfoMeta.from_dict(admin_rankings_upload_info_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


