# AdminSchoolGroup

A user-owned private peer set of schools (admin namespace)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**user** | [**AdminSchoolGroupUser**](AdminSchoolGroupUser.md) |  | [optional] 
**account** | [**AdminSchoolGroupAccount**](AdminSchoolGroupAccount.md) |  | [optional] 
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**school_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_group import AdminSchoolGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolGroup from a JSON string
admin_school_group_instance = AdminSchoolGroup.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolGroup.to_json())

# convert the object into a dict
admin_school_group_dict = admin_school_group_instance.to_dict()
# create an instance of AdminSchoolGroup from a dict
admin_school_group_from_dict = AdminSchoolGroup.from_dict(admin_school_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


