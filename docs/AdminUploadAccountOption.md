# AdminUploadAccountOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_upload_account_option import AdminUploadAccountOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUploadAccountOption from a JSON string
admin_upload_account_option_instance = AdminUploadAccountOption.from_json(json)
# print the JSON string representation of the object
print(AdminUploadAccountOption.to_json())

# convert the object into a dict
admin_upload_account_option_dict = admin_upload_account_option_instance.to_dict()
# create an instance of AdminUploadAccountOption from a dict
admin_upload_account_option_from_dict = AdminUploadAccountOption.from_dict(admin_upload_account_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


