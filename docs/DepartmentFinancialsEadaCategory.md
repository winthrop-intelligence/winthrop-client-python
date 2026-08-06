# DepartmentFinancialsEadaCategory

Suppressed (null) when the source reports no salary, coach count or FTE, when any of them is not positive, or when the salary is negative

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_salary_cents** | **int** | Average annual institutional salary per coach, as reported — never a total pool | 
**coach_count** | **int** |  | 
**fte** | **float** |  | 

## Example

```python
from winthrop_client_python.models.department_financials_eada_category import DepartmentFinancialsEadaCategory

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsEadaCategory from a JSON string
department_financials_eada_category_instance = DepartmentFinancialsEadaCategory.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsEadaCategory.to_json())

# convert the object into a dict
department_financials_eada_category_dict = department_financials_eada_category_instance.to_dict()
# create an instance of DepartmentFinancialsEadaCategory from a dict
department_financials_eada_category_from_dict = DepartmentFinancialsEadaCategory.from_dict(department_financials_eada_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


