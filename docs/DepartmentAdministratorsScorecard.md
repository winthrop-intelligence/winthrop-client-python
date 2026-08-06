# DepartmentAdministratorsScorecard

The administrators' scorecard. The x-axis is the FRS support-staff payroll for the filing year; the y-axis is the Directors' Cup season the cohort actually has on file, which may be labelled by the following year, so both are reported

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_fiscal_year** | **int** |  | 
**results_year** | **int** |  | 
**spend_line** | **str** | Which FRS line backs the money axis | 
**metric** | **str** |  | 
**cohort_size** | **int** |  | 
**points** | [**List[DepartmentAdministratorsScorecardPoint]**](DepartmentAdministratorsScorecardPoint.md) |  | 
**unplotted** | [**List[QuadrantUnplottedSchool]**](QuadrantUnplottedSchool.md) |  | 

## Example

```python
from winthrop_client_python.models.department_administrators_scorecard import DepartmentAdministratorsScorecard

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentAdministratorsScorecard from a JSON string
department_administrators_scorecard_instance = DepartmentAdministratorsScorecard.from_json(json)
# print the JSON string representation of the object
print(DepartmentAdministratorsScorecard.to_json())

# convert the object into a dict
department_administrators_scorecard_dict = department_administrators_scorecard_instance.to_dict()
# create an instance of DepartmentAdministratorsScorecard from a dict
department_administrators_scorecard_from_dict = DepartmentAdministratorsScorecard.from_dict(department_administrators_scorecard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


