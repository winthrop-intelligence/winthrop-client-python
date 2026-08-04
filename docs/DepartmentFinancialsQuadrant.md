# DepartmentFinancialsQuadrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohort_size** | **int** |  | 
**points** | [**List[DepartmentFinancialsQuadrantPoint]**](DepartmentFinancialsQuadrantPoint.md) |  | 
**unplotted** | [**List[DepartmentFinancialsUnplottedSchool]**](DepartmentFinancialsUnplottedSchool.md) |  | 

## Example

```python
from winthrop_client_python.models.department_financials_quadrant import DepartmentFinancialsQuadrant

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsQuadrant from a JSON string
department_financials_quadrant_instance = DepartmentFinancialsQuadrant.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsQuadrant.to_json())

# convert the object into a dict
department_financials_quadrant_dict = department_financials_quadrant_instance.to_dict()
# create an instance of DepartmentFinancialsQuadrant from a dict
department_financials_quadrant_from_dict = DepartmentFinancialsQuadrant.from_dict(department_financials_quadrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


