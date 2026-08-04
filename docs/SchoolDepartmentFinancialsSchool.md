# SchoolDepartmentFinancialsSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**short_name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.school_department_financials_school import SchoolDepartmentFinancialsSchool

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentFinancialsSchool from a JSON string
school_department_financials_school_instance = SchoolDepartmentFinancialsSchool.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentFinancialsSchool.to_json())

# convert the object into a dict
school_department_financials_school_dict = school_department_financials_school_instance.to_dict()
# create an instance of SchoolDepartmentFinancialsSchool from a dict
school_department_financials_school_from_dict = SchoolDepartmentFinancialsSchool.from_dict(school_department_financials_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


