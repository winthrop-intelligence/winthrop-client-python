# AdminSchoolGroupUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_group_user import AdminSchoolGroupUser

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolGroupUser from a JSON string
admin_school_group_user_instance = AdminSchoolGroupUser.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolGroupUser.to_json())

# convert the object into a dict
admin_school_group_user_dict = admin_school_group_user_instance.to_dict()
# create an instance of AdminSchoolGroupUser from a dict
admin_school_group_user_from_dict = AdminSchoolGroupUser.from_dict(admin_school_group_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


