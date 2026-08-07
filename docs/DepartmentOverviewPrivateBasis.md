# DepartmentOverviewPrivateBasis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eada_year** | **int** |  | 
**comp_fiscal_year** | **int** |  | 
**results_year** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_basis import DepartmentOverviewPrivateBasis

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateBasis from a JSON string
department_overview_private_basis_instance = DepartmentOverviewPrivateBasis.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateBasis.to_json())

# convert the object into a dict
department_overview_private_basis_dict = department_overview_private_basis_instance.to_dict()
# create an instance of DepartmentOverviewPrivateBasis from a dict
department_overview_private_basis_from_dict = DepartmentOverviewPrivateBasis.from_dict(department_overview_private_basis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


