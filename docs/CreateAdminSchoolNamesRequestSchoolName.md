# CreateAdminSchoolNamesRequestSchoolName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.create_admin_school_names_request_school_name import CreateAdminSchoolNamesRequestSchoolName

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminSchoolNamesRequestSchoolName from a JSON string
create_admin_school_names_request_school_name_instance = CreateAdminSchoolNamesRequestSchoolName.from_json(json)
# print the JSON string representation of the object
print(CreateAdminSchoolNamesRequestSchoolName.to_json())

# convert the object into a dict
create_admin_school_names_request_school_name_dict = create_admin_school_names_request_school_name_instance.to_dict()
# create an instance of CreateAdminSchoolNamesRequestSchoolName from a dict
create_admin_school_names_request_school_name_from_dict = CreateAdminSchoolNamesRequestSchoolName.from_dict(create_admin_school_names_request_school_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


