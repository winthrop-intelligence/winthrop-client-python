# DepartmentAdministratorsStaffStats

Percentiles over the filed annual amounts, PERCENTILE_CONT interpolation; null when comp is withheld or nothing is filed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**with_comp_count** | **int** |  | 
**median_cents** | **int** |  | 
**p25_cents** | **int** |  | 
**p75_cents** | **int** |  | 
**mean_cents** | **int** |  | 
**estimated** | **bool** | True when 990 amounts are in the pool or some seats carry no comp | 

## Example

```python
from winthrop_client_python.models.department_administrators_staff_stats import DepartmentAdministratorsStaffStats

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsStaffStats from a JSON string
department_administrators_staff_stats_instance = DepartmentAdministratorsStaffStats.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsStaffStats.to_json())

# convert the object into a dict
department_administrators_staff_stats_dict = department_administrators_staff_stats_instance.to_dict()
# create an instance of DepartmentAdministratorsStaffStats from a dict
department_administrators_staff_stats_from_dict = DepartmentAdministratorsStaffStats.from_dict(department_administrators_staff_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


