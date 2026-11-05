# AdminRankingsUploadInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminRankingsUploadInfoMeta**](AdminRankingsUploadInfoMeta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_rankings_upload_info import AdminRankingsUploadInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRankingsUploadInfo from a JSON string
admin_rankings_upload_info_instance = AdminRankingsUploadInfo.from_json(json)
# print the JSON string representation of the object
print(AdminRankingsUploadInfo.to_json())

# convert the object into a dict
admin_rankings_upload_info_dict = admin_rankings_upload_info_instance.to_dict()
# create an instance of AdminRankingsUploadInfo from a dict
admin_rankings_upload_info_from_dict = AdminRankingsUploadInfo.from_dict(admin_rankings_upload_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


