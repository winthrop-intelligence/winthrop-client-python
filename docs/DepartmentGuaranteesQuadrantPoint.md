# DepartmentGuaranteesQuadrantPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**is_subject** | **bool** |  | 
**colors** | **str** |  | 
**paid_cents** | **int** |  | 
**received_cents** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_guarantees_quadrant_point import DepartmentGuaranteesQuadrantPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentGuaranteesQuadrantPoint from a JSON string
department_guarantees_quadrant_point_instance = DepartmentGuaranteesQuadrantPoint.from_json(json)
# print the JSON string representation of the object
print(DepartmentGuaranteesQuadrantPoint.to_json())

# convert the object into a dict
department_guarantees_quadrant_point_dict = department_guarantees_quadrant_point_instance.to_dict()
# create an instance of DepartmentGuaranteesQuadrantPoint from a dict
department_guarantees_quadrant_point_from_dict = DepartmentGuaranteesQuadrantPoint.from_dict(department_guarantees_quadrant_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


