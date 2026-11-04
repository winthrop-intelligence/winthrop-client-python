# AdminGamesUploadStatusMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[AdminGamesImportJob]**](AdminGamesImportJob.md) |  | [optional] 
**required_headers** | **List[str]** |  | [optional] 
**optional_headers** | **List[str]** |  | [optional] 
**sport_names** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_games_upload_status_meta import AdminGamesUploadStatusMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGamesUploadStatusMeta from a JSON string
admin_games_upload_status_meta_instance = AdminGamesUploadStatusMeta.from_json(json)
# print the JSON string representation of the object
print(AdminGamesUploadStatusMeta.to_json())

# convert the object into a dict
admin_games_upload_status_meta_dict = admin_games_upload_status_meta_instance.to_dict()
# create an instance of AdminGamesUploadStatusMeta from a dict
admin_games_upload_status_meta_from_dict = AdminGamesUploadStatusMeta.from_dict(admin_games_upload_status_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


