# DepartmentOverviewResultsGap

Present when the results lens has no data for the selected year, so the page can explain the omission instead of rendering an empty comparison

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lens** | **str** |  | 
**year** | **int** |  | 
**latest_available_year** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_overview_results_gap import DepartmentOverviewResultsGap

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentOverviewResultsGap from a JSON string
department_overview_results_gap_instance = DepartmentOverviewResultsGap.from_json(json)
# print the JSON string representation of the object
print(DepartmentOverviewResultsGap.to_json())

# convert the object into a dict
department_overview_results_gap_dict = department_overview_results_gap_instance.to_dict()
# create an instance of DepartmentOverviewResultsGap from a dict
department_overview_results_gap_from_dict = DepartmentOverviewResultsGap.from_dict(department_overview_results_gap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


