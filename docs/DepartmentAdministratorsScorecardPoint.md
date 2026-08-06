# DepartmentAdministratorsScorecardPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**name** | **str** |  | 
**is_subject** | **bool** |  | 
**colors** | **str** |  | 
**spend_cents** | **int** |  | 
**cup_place** | **int** | Directors&#39; Cup finishing position, scored within division — lower is better | 

## Example

```python
from winthrop_client_python.models.department_administrators_scorecard_point import DepartmentAdministratorsScorecardPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsScorecardPoint from a JSON string
department_administrators_scorecard_point_instance = DepartmentAdministratorsScorecardPoint.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsScorecardPoint.to_json())

# convert the object into a dict
department_administrators_scorecard_point_dict = department_administrators_scorecard_point_instance.to_dict()
# create an instance of DepartmentAdministratorsScorecardPoint from a dict
department_administrators_scorecard_point_from_dict = DepartmentAdministratorsScorecardPoint.from_dict(department_administrators_scorecard_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


