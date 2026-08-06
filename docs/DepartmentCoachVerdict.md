# DepartmentCoachVerdict


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**pay_rank** | **int** |  | 
**finish_rank** | **int** |  | 
**delta** | **int** |  | 
**first_year** | **bool** |  | 
**contract_year** | **int** |  | 
**contract_length_years** | **int** |  | 
**approximate** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_coach_verdict import DepartmentCoachVerdict

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentCoachVerdict from a JSON string
department_coach_verdict_instance = DepartmentCoachVerdict.from_json(json)
# print the JSON string representation of the object
print(DepartmentCoachVerdict.to_json())

# convert the object into a dict
department_coach_verdict_dict = department_coach_verdict_instance.to_dict()
# create an instance of DepartmentCoachVerdict from a dict
department_coach_verdict_from_dict = DepartmentCoachVerdict.from_dict(department_coach_verdict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


