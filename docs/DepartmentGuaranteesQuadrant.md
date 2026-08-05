# DepartmentGuaranteesQuadrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cohort_size** | **int** |  | 
**points** | [**List[DepartmentGuaranteesQuadrantPoint]**](DepartmentGuaranteesQuadrantPoint.md) |  | 
**unplotted** | [**List[DepartmentFinancialsUnplottedSchool]**](DepartmentFinancialsUnplottedSchool.md) |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_quadrant import DepartmentGuaranteesQuadrant

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesQuadrant from a JSON string
department_guarantees_quadrant_instance = DepartmentGuaranteesQuadrant.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesQuadrant.to_json())

# convert the object into a dict
department_guarantees_quadrant_dict = department_guarantees_quadrant_instance.to_dict()
# create an instance of DepartmentGuaranteesQuadrant from a dict
department_guarantees_quadrant_from_dict = DepartmentGuaranteesQuadrant.from_dict(department_guarantees_quadrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


