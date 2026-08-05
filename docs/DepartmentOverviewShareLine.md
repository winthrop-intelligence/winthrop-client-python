# DepartmentOverviewShareLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**amount_cents** | **int** |  | 
**highlight** | **bool** |  | 
**share** | **float** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_share_line import DepartmentOverviewShareLine

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewShareLine from a JSON string
department_overview_share_line_instance = DepartmentOverviewShareLine.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewShareLine.to_json())

# convert the object into a dict
department_overview_share_line_dict = department_overview_share_line_instance.to_dict()
# create an instance of DepartmentOverviewShareLine from a dict
department_overview_share_line_from_dict = DepartmentOverviewShareLine.from_dict(department_overview_share_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


