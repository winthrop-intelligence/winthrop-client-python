# DepartmentGuaranteesFiledLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**expense_cents** | **int** |  | 
**revenue_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_filed_line import DepartmentGuaranteesFiledLine

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesFiledLine from a JSON string
department_guarantees_filed_line_instance = DepartmentGuaranteesFiledLine.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesFiledLine.to_json())

# convert the object into a dict
department_guarantees_filed_line_dict = department_guarantees_filed_line_instance.to_dict()
# create an instance of DepartmentGuaranteesFiledLine from a dict
department_guarantees_filed_line_from_dict = DepartmentGuaranteesFiledLine.from_dict(department_guarantees_filed_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


