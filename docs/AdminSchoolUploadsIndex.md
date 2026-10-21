# AdminSchoolUploadsIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminSchoolUploadsIndexMeta**](AdminSchoolUploadsIndexMeta.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_uploads_index import AdminSchoolUploadsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolUploadsIndex from a JSON string
admin_school_uploads_index_instance = AdminSchoolUploadsIndex.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolUploadsIndex.to_json())

# convert the object into a dict
admin_school_uploads_index_dict = admin_school_uploads_index_instance.to_dict()
# create an instance of AdminSchoolUploadsIndex from a dict
admin_school_uploads_index_from_dict = AdminSchoolUploadsIndex.from_dict(admin_school_uploads_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


