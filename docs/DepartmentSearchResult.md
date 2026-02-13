# DepartmentSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**division_name** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 
**usnwr_ranking** | **int** |  | [optional] 
**directors_cup_ranking** | **int** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**nickname** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.department_search_result import DepartmentSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentSearchResult from a JSON string
department_search_result_instance = DepartmentSearchResult.from_json(json)
# print the JSON string representation of the object
print(DepartmentSearchResult.to_json())

# convert the object into a dict
department_search_result_dict = department_search_result_instance.to_dict()
# create an instance of DepartmentSearchResult from a dict
department_search_result_from_dict = DepartmentSearchResult.from_dict(department_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


