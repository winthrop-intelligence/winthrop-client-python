# DepartmentSearchResultDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_name** | **str** |  | [optional] 
**ad_coach_id** | **int** |  | [optional] 
**ad_salary_cents** | **int** |  | [optional] 
**revenue_cents** | **int** |  | [optional] 
**expense_cents** | **int** |  | [optional] 
**deals** | [**List[DepartmentSearchResultDepartmentDealsInner]**](DepartmentSearchResultDepartmentDealsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_search_result_department import DepartmentSearchResultDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentSearchResultDepartment from a JSON string
department_search_result_department_instance = DepartmentSearchResultDepartment.from_json(json)
# print the JSON string representation of the object
print(DepartmentSearchResultDepartment.to_json())

# convert the object into a dict
department_search_result_department_dict = department_search_result_department_instance.to_dict()
# create an instance of DepartmentSearchResultDepartment from a dict
department_search_result_department_from_dict = DepartmentSearchResultDepartment.from_dict(department_search_result_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


