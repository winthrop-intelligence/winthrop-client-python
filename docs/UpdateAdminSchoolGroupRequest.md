# UpdateAdminSchoolGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_group** | [**UpdateSchoolGroupRequestSchoolGroup**](UpdateSchoolGroupRequestSchoolGroup.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_school_group_request import UpdateAdminSchoolGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminSchoolGroupRequest from a JSON string
update_admin_school_group_request_instance = UpdateAdminSchoolGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminSchoolGroupRequest.to_json())

# convert the object into a dict
update_admin_school_group_request_dict = update_admin_school_group_request_instance.to_dict()
# create an instance of UpdateAdminSchoolGroupRequest from a dict
update_admin_school_group_request_from_dict = UpdateAdminSchoolGroupRequest.from_dict(update_admin_school_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


