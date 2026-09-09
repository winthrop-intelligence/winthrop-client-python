# DepartmentSearchResultDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_status** | **str** |  | [optional] 
**ad_name** | **str** |  | [optional] 
**ad_coach_id** | **int** |  | [optional] 
**ad_salary_cents** | **int** |  | [optional] 
**financials_reported** | **bool** | Whether this row&#39;s own source reported figures: NCAA FRS for a public school, EADA for a private one (WINAD-10383). Not \&quot;does any source hold figures\&quot; — a public school with no FRS filing is false even where an EADA filing exists, because public rows do not fall back. | [optional] 
**financials_basis** | **str** | Which report revenue_cents/expense_cents were read from. Public schools report NCAA FRS and never fall back; private schools report EADA, and their FRS figures are suppressed for every viewer. Null when the row&#39;s source reported nothing, and also when the viewer&#39;s subscription does not carry EADA for that school. | [optional] 
**financials_basis_year** | **int** | The filing year those figures come from: the list&#39;s financials_year when the school filed it, otherwise that school&#39;s newest filing. An EADA row can therefore report a year the rest of the page is not on. | [optional] 
**revenue_cents** | **int** |  | [optional] 
**expense_cents** | **int** |  | [optional] 
**football_revenue_cents** | **int** | EADA sport-split revenue; null on an FRS row. | [optional] 
**mens_basketball_revenue_cents** | **int** | EADA sport-split revenue; null on an FRS row. | [optional] 
**budget_rank** | **int** |  | [optional] 
**budget_rank_of** | **int** |  | [optional] 
**budget_rank_conference_name** | **str** |  | [optional] 
**deals** | [**List[DepartmentSearchResultDepartmentDealsInner]**](DepartmentSearchResultDepartmentDealsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_search_result_department import DepartmentSearchResultDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentSearchResultDepartment from a JSON string
department_search_result_department_instance = DepartmentSearchResultDepartment.from_json(json)
# print the JSON string representation of the object
print(DepartmentSearchResultDepartment.to_json())

# convert the object into a dict
department_search_result_department_dict = department_search_result_department_instance.to_dict()
# create an instance of DepartmentSearchResultDepartment from a dict
department_search_result_department_from_dict = DepartmentSearchResultDepartment.from_dict(department_search_result_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


