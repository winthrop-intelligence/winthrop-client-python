# DepartmentFinancialsUnplottedSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_financials_unplotted_school import DepartmentFinancialsUnplottedSchool

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsUnplottedSchool from a JSON string
department_financials_unplotted_school_instance = DepartmentFinancialsUnplottedSchool.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsUnplottedSchool.to_json())

# convert the object into a dict
department_financials_unplotted_school_dict = department_financials_unplotted_school_instance.to_dict()
# create an instance of DepartmentFinancialsUnplottedSchool from a dict
department_financials_unplotted_school_from_dict = DepartmentFinancialsUnplottedSchool.from_dict(department_financials_unplotted_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


