# AdminUpload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**account_id** | **int** |  | 
**account_name** | **str** |  | 
**filename** | **str** | Active Storage filename of the uploaded PDF | [optional] 
**file_url** | **str** | URL of the uploaded file | [optional] 
**user_name** | **str** |  | [optional] 
**archived** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.admin_upload import AdminUpload

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUpload from a JSON string
admin_upload_instance = AdminUpload.from_json(json)
# print the JSON string representation of the object
print(AdminUpload.to_json())

# convert the object into a dict
admin_upload_dict = admin_upload_instance.to_dict()
# create an instance of AdminUpload from a dict
admin_upload_from_dict = AdminUpload.from_dict(admin_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


