# DepartmentOverviewResultsQuadrant

One fiscal year of spending against the selected Directors' Cup season. Fiscal year is season ending year minus one; only the current season may fall back one year. Private subjects use EADA for all peers; public subjects prefer FRS per dot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eada_fallback_count** | **int** | Number of plotted dots using EADA instead of FRS in public mode; zero in private mode | 
**basis** | **str** |  | 
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


