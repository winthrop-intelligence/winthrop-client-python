# DepartmentStaffSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**staff** | [**List[DepartmentStaffMember]**](DepartmentStaffMember.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_staff_school import DepartmentStaffSchool

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentStaffSchool from a JSON string
department_staff_school_instance = DepartmentStaffSchool.from_json(json)
# print the JSON string representation of the object
print(DepartmentStaffSchool.to_json())

# convert the object into a dict
department_staff_school_dict = department_staff_school_instance.to_dict()
# create an instance of DepartmentStaffSchool from a dict
department_staff_school_from_dict = DepartmentStaffSchool.from_dict(department_staff_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


