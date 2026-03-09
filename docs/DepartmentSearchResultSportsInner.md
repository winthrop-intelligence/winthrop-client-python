# DepartmentSearchResultSportsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_name** | **str** |  | [optional] 
**sport_key** | **str** |  | [optional] 
**head_coach_name** | **str** |  | [optional] 
**head_coach_id** | **int** |  | [optional] 
**head_coach_salary_cents** | **int** |  | [optional] 
**asst_pool_cents** | **int** |  | [optional] 
**revenue_cents** | **int** |  | [optional] 
**expense_cents** | **int** |  | [optional] 
**avg_guarantee_paid_cents** | **int** |  | [optional] 
**avg_guarantee_received_cents** | **int** |  | [optional] 
**record** | **str** |  | [optional] 
**conference_record** | **str** |  | [optional] 
**rpi** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_search_result_sports_inner import DepartmentSearchResultSportsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentSearchResultSportsInner from a JSON string
department_search_result_sports_inner_instance = DepartmentSearchResultSportsInner.from_json(json)
# print the JSON string representation of the object
print(DepartmentSearchResultSportsInner.to_json())

# convert the object into a dict
department_search_result_sports_inner_dict = department_search_result_sports_inner_instance.to_dict()
# create an instance of DepartmentSearchResultSportsInner from a dict
department_search_result_sports_inner_from_dict = DepartmentSearchResultSportsInner.from_dict(department_search_result_sports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


