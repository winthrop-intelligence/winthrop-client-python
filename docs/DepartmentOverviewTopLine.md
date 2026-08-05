# DepartmentOverviewTopLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**amount_cents** | **int** |  | 
**share** | **float** | Percentage of the ledger total | 

## Example

```python
from winthrop_client_python.models.department_overview_top_line import DepartmentOverviewTopLine

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewTopLine from a JSON string
department_overview_top_line_instance = DepartmentOverviewTopLine.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewTopLine.to_json())

# convert the object into a dict
department_overview_top_line_dict = department_overview_top_line_instance.to_dict()
# create an instance of DepartmentOverviewTopLine from a dict
department_overview_top_line_from_dict = DepartmentOverviewTopLine.from_dict(department_overview_top_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


