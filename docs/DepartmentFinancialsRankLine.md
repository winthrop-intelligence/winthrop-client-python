# DepartmentFinancialsRankLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**label** | **str** |  | 
**amount_cents** | **int** |  | 
**rank** | **int** |  | 
**cohort_size** | **int** |  | 
**partial_cohort** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.department_financials_rank_line import DepartmentFinancialsRankLine

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentFinancialsRankLine from a JSON string
department_financials_rank_line_instance = DepartmentFinancialsRankLine.from_json(json)
# print the JSON string representation of the object
print(DepartmentFinancialsRankLine.to_json())

# convert the object into a dict
department_financials_rank_line_dict = department_financials_rank_line_instance.to_dict()
# create an instance of DepartmentFinancialsRankLine from a dict
department_financials_rank_line_from_dict = DepartmentFinancialsRankLine.from_dict(department_financials_rank_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


