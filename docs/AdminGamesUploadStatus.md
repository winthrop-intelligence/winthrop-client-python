# AdminGamesUploadStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminGamesUploadStatusMeta**](AdminGamesUploadStatusMeta.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_games_upload_status import AdminGamesUploadStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGamesUploadStatus from a JSON string
admin_games_upload_status_instance = AdminGamesUploadStatus.from_json(json)
# print the JSON string representation of the object
print(AdminGamesUploadStatus.to_json())

# convert the object into a dict
admin_games_upload_status_dict = admin_games_upload_status_instance.to_dict()
# create an instance of AdminGamesUploadStatus from a dict
admin_games_upload_status_from_dict = AdminGamesUploadStatus.from_dict(admin_games_upload_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


