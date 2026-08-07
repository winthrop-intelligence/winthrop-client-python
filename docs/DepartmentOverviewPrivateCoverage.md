# DepartmentOverviewPrivateCoverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**percent** | **int** |  | 
**provisional** | **bool** | True while the coverage metric is undefined; the value is pinned at 0. | 

## Example

```python
from winthrop_client_python.models.department_overview_private_coverage import DepartmentOverviewPrivateCoverage

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateCoverage from a JSON string
department_overview_private_coverage_instance = DepartmentOverviewPrivateCoverage.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateCoverage.to_json())

# convert the object into a dict
department_overview_private_coverage_dict = department_overview_private_coverage_instance.to_dict()
# create an instance of DepartmentOverviewPrivateCoverage from a dict
department_overview_private_coverage_from_dict = DepartmentOverviewPrivateCoverage.from_dict(department_overview_private_coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


