# DepartmentCoachesQuadrant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_fiscal_year** | **int** |  | 
**spend_cohort** | **str** |  | 
**plotted_count** | **int** |  | 
**seat_count** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_coaches_quadrant import DepartmentCoachesQuadrant

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesQuadrant from a JSON string
department_coaches_quadrant_instance = DepartmentCoachesQuadrant.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesQuadrant.to_json())

# convert the object into a dict
department_coaches_quadrant_dict = department_coaches_quadrant_instance.to_dict()
# create an instance of DepartmentCoachesQuadrant from a dict
department_coaches_quadrant_from_dict = DepartmentCoachesQuadrant.from_dict(department_coaches_quadrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


