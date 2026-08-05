# DepartmentOverviewQuadrantPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**is_subject** | **bool** |  | 
**colors** | **str** |  | 
**exp_total_cents** | **int** |  | 
**cup_place** | **int** | Directors&#39; Cup finishing position, scored within division — lower is better | 

## Example

```python
from winthrop_client_python.models.department_overview_quadrant_point import DepartmentOverviewQuadrantPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewQuadrantPoint from a JSON string
department_overview_quadrant_point_instance = DepartmentOverviewQuadrantPoint.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewQuadrantPoint.to_json())

# convert the object into a dict
department_overview_quadrant_point_dict = department_overview_quadrant_point_instance.to_dict()
# create an instance of DepartmentOverviewQuadrantPoint from a dict
department_overview_quadrant_point_from_dict = DepartmentOverviewQuadrantPoint.from_dict(department_overview_quadrant_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


