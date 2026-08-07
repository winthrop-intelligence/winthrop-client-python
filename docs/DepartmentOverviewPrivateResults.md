# DepartmentOverviewPrivateResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**place** | **int** |  | 
**year** | **int** |  | 
**basis** | **str** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_private_results import DepartmentOverviewPrivateResults

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewPrivateResults from a JSON string
department_overview_private_results_instance = DepartmentOverviewPrivateResults.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewPrivateResults.to_json())

# convert the object into a dict
department_overview_private_results_dict = department_overview_private_results_instance.to_dict()
# create an instance of DepartmentOverviewPrivateResults from a dict
department_overview_private_results_from_dict = DepartmentOverviewPrivateResults.from_dict(department_overview_private_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


