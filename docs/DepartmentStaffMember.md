# DepartmentStaffMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**total_comp** | **int** |  | [optional] 
**position_title** | **str** |  | [optional] 
**photo_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_staff_member import DepartmentStaffMember

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentStaffMember from a JSON string
department_staff_member_instance = DepartmentStaffMember.from_json(json)
# print the JSON string representation of the object
print(DepartmentStaffMember.to_json())

# convert the object into a dict
department_staff_member_dict = department_staff_member_instance.to_dict()
# create an instance of DepartmentStaffMember from a dict
department_staff_member_from_dict = DepartmentStaffMember.from_dict(department_staff_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


