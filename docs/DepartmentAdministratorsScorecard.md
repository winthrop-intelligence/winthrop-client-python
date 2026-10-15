# DepartmentAdministratorsScorecard

The administrators' scorecard uses FRS support-staff payroll for public subjects and EADA expense not allocated by team for private subjects. Money reads the fiscal year before the selected season; only the current season may fall back one year. Cup standings read only the selected season. Missing standings produce a gap, including for the current season; the financial-year fallback never applies to results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spend_basis** | **str** |  | 
**spend_fiscal_year** | **int** |  | 
**results_year** | **int** |  | 
**spend_line** | **str** | The money line; EADA unallocated expense includes overhead and facilities, broader than payroll | 
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


