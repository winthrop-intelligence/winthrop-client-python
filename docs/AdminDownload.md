# AdminDownload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**asset_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_download import AdminDownload

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDownload from a JSON string
admin_download_instance = AdminDownload.from_json(json)
# print the JSON string representation of the object
print(AdminDownload.to_json())

# convert the object into a dict
admin_download_dict = admin_download_instance.to_dict()
# create an instance of AdminDownload from a dict
admin_download_from_dict = AdminDownload.from_dict(admin_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


