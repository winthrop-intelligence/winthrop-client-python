# SchoolDepartmentFinancials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**SchoolDepartmentOverviewSchool**](SchoolDepartmentOverviewSchool.md) |  | 
**conference** | [**SchoolDepartmentOverviewConference**](SchoolDepartmentOverviewConference.md) |  | 
**latest_filed_year** | **int** |  | 
**selected_year** | **int** |  | 
**available_years** | **List[int]** |  | 
**quadrant** | [**DepartmentFinancialsQuadrant**](DepartmentFinancialsQuadrant.md) |  | 
**net_result** | [**DepartmentFinancialsNetResult**](DepartmentFinancialsNetResult.md) |  | 
**ranks** | [**List[DepartmentFinancialsRankLine]**](DepartmentFinancialsRankLine.md) |  | 
**revenue** | [**DepartmentFinancialsLedger**](DepartmentFinancialsLedger.md) |  | 
**expenses** | [**DepartmentFinancialsLedger**](DepartmentFinancialsLedger.md) |  | 
**trend** | [**List[DepartmentFinancialsTrendEntry]**](DepartmentFinancialsTrendEntry.md) |  | 

## Example

```python
from winthrop_client_python.models.school_department_financials import SchoolDepartmentFinancials

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentFinancials from a JSON string
school_department_financials_instance = SchoolDepartmentFinancials.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentFinancials.to_json())

# convert the object into a dict
school_department_financials_dict = school_department_financials_instance.to_dict()
# create an instance of SchoolDepartmentFinancials from a dict
school_department_financials_from_dict = SchoolDepartmentFinancials.from_dict(school_department_financials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


