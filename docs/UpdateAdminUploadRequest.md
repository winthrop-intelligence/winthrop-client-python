# UpdateAdminUploadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload** | [**UpdateAdminUploadRequestUpload**](UpdateAdminUploadRequestUpload.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_upload_request import UpdateAdminUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminUploadRequest from a JSON string
update_admin_upload_request_instance = UpdateAdminUploadRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminUploadRequest.to_json())

# convert the object into a dict
update_admin_upload_request_dict = update_admin_upload_request_instance.to_dict()
# create an instance of UpdateAdminUploadRequest from a dict
update_admin_upload_request_from_dict = UpdateAdminUploadRequest.from_dict(update_admin_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


