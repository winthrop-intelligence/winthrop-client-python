# DepartmentCoachResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**conference_wins** | **int** |  | 
**conference_losses** | **int** |  | 
**metric** | **str** |  | 
**metric_rank** | **int** |  | 
**metric_year** | **int** |  | 
**postseason** | **str** |  | 
**champion** | **bool** |  | 
**finish_rank** | **int** |  | 
**finish_cohort** | **int** |  | 

## Example

```python
from winthrop_client_python.models.department_coach_result import DepartmentCoachResult

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachResult from a JSON string
department_coach_result_instance = DepartmentCoachResult.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachResult.to_json())

# convert the object into a dict
department_coach_result_dict = department_coach_result_instance.to_dict()
# create an instance of DepartmentCoachResult from a dict
department_coach_result_from_dict = DepartmentCoachResult.from_dict(department_coach_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


