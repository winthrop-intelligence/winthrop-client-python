# UpdateAdminSchoolNamesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | [**UpdateAdminSchoolNamesRequestSchoolName**](UpdateAdminSchoolNamesRequestSchoolName.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_school_names_request import UpdateAdminSchoolNamesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminSchoolNamesRequest from a JSON string
update_admin_school_names_request_instance = UpdateAdminSchoolNamesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminSchoolNamesRequest.to_json())

# convert the object into a dict
update_admin_school_names_request_dict = update_admin_school_names_request_instance.to_dict()
# create an instance of UpdateAdminSchoolNamesRequest from a dict
update_admin_school_names_request_from_dict = UpdateAdminSchoolNamesRequest.from_dict(update_admin_school_names_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


