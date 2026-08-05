# SchoolDepartmentOverviewSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.school_department_overview_school import SchoolDepartmentOverviewSchool

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentOverviewSchool from a JSON string
school_department_overview_school_instance = SchoolDepartmentOverviewSchool.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentOverviewSchool.to_json())

# convert the object into a dict
school_department_overview_school_dict = school_department_overview_school_instance.to_dict()
# create an instance of SchoolDepartmentOverviewSchool from a dict
school_department_overview_school_from_dict = SchoolDepartmentOverviewSchool.from_dict(school_department_overview_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


