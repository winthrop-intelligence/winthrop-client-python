# DepartmentFinancialsEadaCoaching

EADA institution-wide coaching aggregates. Public federal data, so it is not subject to NCAA cashflow suppression and is present for private schools too

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**total_salary_pool_cents** | **int** | Derived as the sum of each displayed average multiplied by its coach count | 
**head_coach** | [**DepartmentFinancialsEadaRole**](DepartmentFinancialsEadaRole.md) |  | 
**assistant_coach** | [**DepartmentFinancialsEadaRole**](DepartmentFinancialsEadaRole.md) |  | 

## Example

```python
from winthrop_client_python.models.department_financials_eada_coaching import DepartmentFinancialsEadaCoaching

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsEadaCoaching from a JSON string
department_financials_eada_coaching_instance = DepartmentFinancialsEadaCoaching.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsEadaCoaching.to_json())

# convert the object into a dict
department_financials_eada_coaching_dict = department_financials_eada_coaching_instance.to_dict()
# create an instance of DepartmentFinancialsEadaCoaching from a dict
department_financials_eada_coaching_from_dict = DepartmentFinancialsEadaCoaching.from_dict(department_financials_eada_coaching_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


