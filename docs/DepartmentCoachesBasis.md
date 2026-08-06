# DepartmentCoachesBasis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payroll_cents** | **int** |  | 
**payroll_source** | **str** |  | 
**payroll_fiscal_year** | **int** |  | 
**comp_fiscal_year** | **int** |  | 
**seats_with_comp** | **int** |  | 
**seats_pending_verification** | **int** |  | 
**contracts_on_file** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_coaches_basis import DepartmentCoachesBasis

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesBasis from a JSON string
department_coaches_basis_instance = DepartmentCoachesBasis.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesBasis.to_json())

# convert the object into a dict
department_coaches_basis_dict = department_coaches_basis_instance.to_dict()
# create an instance of DepartmentCoachesBasis from a dict
department_coaches_basis_from_dict = DepartmentCoachesBasis.from_dict(department_coaches_basis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


