# CreateAdminSchoolNamesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_name** | [**CreateAdminSchoolNamesRequestSchoolName**](CreateAdminSchoolNamesRequestSchoolName.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_school_names_request import CreateAdminSchoolNamesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminSchoolNamesRequest from a JSON string
create_admin_school_names_request_instance = CreateAdminSchoolNamesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminSchoolNamesRequest.to_json())

# convert the object into a dict
create_admin_school_names_request_dict = create_admin_school_names_request_instance.to_dict()
# create an instance of CreateAdminSchoolNamesRequest from a dict
create_admin_school_names_request_from_dict = CreateAdminSchoolNamesRequest.from_dict(create_admin_school_names_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


