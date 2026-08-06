# DepartmentAdministratorsBasis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | 
**staff_count** | **int** |  | 
**with_comp_count** | **int** |  | 
**filed_990_count** | **int** |  | 
**hourly_excluded_count** | **int** | Hourly rows stay on the roster but out of every dollar aggregate | 
**comp_visible** | **bool** |  | 
**comp_fiscal_year** | **int** | Private mode only — the newest 990 filing year on the officer lines | 

## Example

```python
from winthrop_client_python.models.department_administrators_basis import DepartmentAdministratorsBasis

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsBasis from a JSON string
department_administrators_basis_instance = DepartmentAdministratorsBasis.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsBasis.to_json())

# convert the object into a dict
department_administrators_basis_dict = department_administrators_basis_instance.to_dict()
# create an instance of DepartmentAdministratorsBasis from a dict
department_administrators_basis_from_dict = DepartmentAdministratorsBasis.from_dict(department_administrators_basis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


