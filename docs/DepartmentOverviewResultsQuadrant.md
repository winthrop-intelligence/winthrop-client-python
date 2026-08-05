# DepartmentOverviewResultsQuadrant

Spend against results. The x-axis is the selected filing year; the y-axis is the Directors' Cup season the cohort actually has on file, which may be labelled by the following year, so both are reported

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_year** | **int** |  | 
**results_year** | **int** |  | 
**metric** | **str** |  | 
**cohort_size** | **int** |  | 
**points** | [**List[DepartmentOverviewQuadrantPoint]**](DepartmentOverviewQuadrantPoint.md) |  | 
**unplotted** | [**List[DepartmentOverviewUnplottedSchool]**](DepartmentOverviewUnplottedSchool.md) |  | 

## Example

```python
from winthrop_client_python.models.department_overview_results_quadrant import DepartmentOverviewResultsQuadrant

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewResultsQuadrant from a JSON string
department_overview_results_quadrant_instance = DepartmentOverviewResultsQuadrant.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewResultsQuadrant.to_json())

# convert the object into a dict
department_overview_results_quadrant_dict = department_overview_results_quadrant_instance.to_dict()
# create an instance of DepartmentOverviewResultsQuadrant from a dict
department_overview_results_quadrant_from_dict = DepartmentOverviewResultsQuadrant.from_dict(department_overview_results_quadrant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


