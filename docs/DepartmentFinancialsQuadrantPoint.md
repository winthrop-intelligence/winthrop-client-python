# DepartmentFinancialsQuadrantPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**is_subject** | **bool** |  | 
**colors** | **str** |  | 
**exp_total_cents** | **int** |  | 
**rev_total_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_financials_quadrant_point import DepartmentFinancialsQuadrantPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsQuadrantPoint from a JSON string
department_financials_quadrant_point_instance = DepartmentFinancialsQuadrantPoint.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsQuadrantPoint.to_json())

# convert the object into a dict
department_financials_quadrant_point_dict = department_financials_quadrant_point_instance.to_dict()
# create an instance of DepartmentFinancialsQuadrantPoint from a dict
department_financials_quadrant_point_from_dict = DepartmentFinancialsQuadrantPoint.from_dict(department_financials_quadrant_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


