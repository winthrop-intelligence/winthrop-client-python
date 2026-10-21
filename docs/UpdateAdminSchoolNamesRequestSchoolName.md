# UpdateAdminSchoolNamesRequestSchoolName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_school_names_request_school_name import UpdateAdminSchoolNamesRequestSchoolName

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminSchoolNamesRequestSchoolName from a JSON string
update_admin_school_names_request_school_name_instance = UpdateAdminSchoolNamesRequestSchoolName.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminSchoolNamesRequestSchoolName.to_json())

# convert the object into a dict
update_admin_school_names_request_school_name_dict = update_admin_school_names_request_school_name_instance.to_dict()
# create an instance of UpdateAdminSchoolNamesRequestSchoolName from a dict
update_admin_school_names_request_school_name_from_dict = UpdateAdminSchoolNamesRequestSchoolName.from_dict(update_admin_school_names_request_school_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


