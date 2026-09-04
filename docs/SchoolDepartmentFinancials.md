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
**ranks** | [**List[DepartmentFinancialsRankLine]**](DepartmentFinancialsRankLine.md) | Per-line conference ranks. Line keys depend on the subject&#39;s basis: FRS lines for a public school; for a private school the EADA lines (total_expenses, total_revenue, coaching_salaries, student_aid, recruiting, net_result), ranked against every peer with a matched EADA report for the year. | 
**ranks_filed_count** | **int** | How many conference members filed the report the ranks read, for the selected year and on the subject&#39;s own basis. A rank line&#39;s cohort_size counts only the members reporting that line, so this is the only figure that says whether the whole conference is in the comparison — which is what the private page&#39;s \&quot;every school files EADA\&quot; caption claims (WINAD-10401). Null with no selected year. | 
**revenue** | [**DepartmentFinancialsLedger**](DepartmentFinancialsLedger.md) |  | 
**expenses** | [**DepartmentFinancialsLedger**](DepartmentFinancialsLedger.md) |  | 
**trend** | [**List[DepartmentFinancialsTrendEntry]**](DepartmentFinancialsTrendEntry.md) | One entry per window year on the subject&#39;s basis — FRS totals for a public school (non-latest filings provisional), EADA totals for a private school (never provisional). | 
**officers_990_count** | **int** | How many officers the school&#39;s newest IRS 990 filing names — the private-school footer&#39;s pointer to where per-coach comp lives (WINAD-10393). Null for a public school, when no 990 comp is on file, or when the viewer lacks the administrator_compensation ability. | 
**eada_ledger** | [**DepartmentFinancialsEadaLedger**](DepartmentFinancialsEadaLedger.md) |  | 
**eada_coaching** | [**DepartmentFinancialsEadaCoaching**](DepartmentFinancialsEadaCoaching.md) |  | 

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


