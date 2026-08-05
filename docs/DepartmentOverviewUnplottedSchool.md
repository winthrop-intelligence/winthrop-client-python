# DepartmentOverviewUnplottedSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**reason** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_unplotted_school import DepartmentOverviewUnplottedSchool

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewUnplottedSchool from a JSON string
department_overview_unplotted_school_instance = DepartmentOverviewUnplottedSchool.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewUnplottedSchool.to_json())

# convert the object into a dict
department_overview_unplotted_school_dict = department_overview_unplotted_school_instance.to_dict()
# create an instance of DepartmentOverviewUnplottedSchool from a dict
department_overview_unplotted_school_from_dict = DepartmentOverviewUnplottedSchool.from_dict(department_overview_unplotted_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


