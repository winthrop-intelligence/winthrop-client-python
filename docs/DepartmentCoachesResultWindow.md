# DepartmentCoachesResultWindow

Season-year bounds the results lens may read from — the client renders the results-axis label from these instead of recreating the window policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_year** | **int** |  | 
**end_year** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_coaches_result_window import DepartmentCoachesResultWindow

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachesResultWindow from a JSON string
department_coaches_result_window_instance = DepartmentCoachesResultWindow.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachesResultWindow.to_json())

# convert the object into a dict
department_coaches_result_window_dict = department_coaches_result_window_instance.to_dict()
# create an instance of DepartmentCoachesResultWindow from a dict
department_coaches_result_window_from_dict = DepartmentCoachesResultWindow.from_dict(department_coaches_result_window_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


