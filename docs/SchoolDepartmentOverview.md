# SchoolDepartmentOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**SchoolDepartmentOverviewSchool**](SchoolDepartmentOverviewSchool.md) |  | 
**conference** | [**SchoolDepartmentOverviewConference**](SchoolDepartmentOverviewConference.md) |  | 
**latest_filed_year** | **int** |  | 
**selected_year** | **int** |  | 
**available_years** | **List[int]** |  | 
**results_quadrant** | [**DepartmentOverviewResultsQuadrant**](DepartmentOverviewResultsQuadrant.md) |  | 
**headline_stats** | [**List[DepartmentOverviewHeadlineStat]**](DepartmentOverviewHeadlineStat.md) |  | 
**flow_summary** | [**DepartmentOverviewFlowSummary**](DepartmentOverviewFlowSummary.md) |  | 
**top_revenue_lines** | [**List[DepartmentOverviewTopLine]**](DepartmentOverviewTopLine.md) |  | 
**top_expense_lines** | [**List[DepartmentOverviewTopLine]**](DepartmentOverviewTopLine.md) |  | 
**dollar_shares** | [**DepartmentOverviewDollarShares**](DepartmentOverviewDollarShares.md) |  | 
**provenance** | [**DepartmentOverviewProvenance**](DepartmentOverviewProvenance.md) |  | 
**results_gap** | [**DepartmentOverviewResultsGap**](DepartmentOverviewResultsGap.md) |  | 
**mode** | **str** | Which basis the tab renders. A private school has no FRS filing, so every FRS-derived module is null and the private_* modules carry the page. | [optional] 
**private_spend** | [**DepartmentOverviewPrivateSpend**](DepartmentOverviewPrivateSpend.md) |  | [optional] 
**private_results** | [**DepartmentOverviewPrivateResults**](DepartmentOverviewPrivateResults.md) |  | [optional] 
**private_coverage** | [**DepartmentOverviewPrivateCoverage**](DepartmentOverviewPrivateCoverage.md) |  | [optional] 
**private_disclosure** | [**DepartmentOverviewPrivateDisclosure**](DepartmentOverviewPrivateDisclosure.md) |  | [optional] 
**private_ad** | [**DepartmentOverviewPrivateAd**](DepartmentOverviewPrivateAd.md) |  | [optional] 
**private_basis** | [**DepartmentOverviewPrivateBasis**](DepartmentOverviewPrivateBasis.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.school_department_overview import SchoolDepartmentOverview

# TODO update the JSON string below
json = "{}"
# create an instance of SchoolDepartmentOverview from a JSON string
school_department_overview_instance = SchoolDepartmentOverview.from_json(json)
# print the JSON string representation of the object
print(SchoolDepartmentOverview.to_json())

# convert the object into a dict
school_department_overview_dict = school_department_overview_instance.to_dict()
# create an instance of SchoolDepartmentOverview from a dict
school_department_overview_from_dict = SchoolDepartmentOverview.from_dict(school_department_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


