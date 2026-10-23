# AdminUploadsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**accounts** | [**List[AdminUploadAccountOption]**](AdminUploadAccountOption.md) | Accounts that have uploads, ordered by name (the Account filter&#39;s options) | 
**data** | [**List[AdminUpload]**](AdminUpload.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_uploads_list import AdminUploadsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUploadsList from a JSON string
admin_uploads_list_instance = AdminUploadsList.from_json(json)
# print the JSON string representation of the object
print(AdminUploadsList.to_json())

# convert the object into a dict
admin_uploads_list_dict = admin_uploads_list_instance.to_dict()
# create an instance of AdminUploadsList from a dict
admin_uploads_list_from_dict = AdminUploadsList.from_dict(admin_uploads_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


