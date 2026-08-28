# FinancialComparisonRankedRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank** | **int** |  | 
**school_id** | **int** |  | 
**school_name** | **str** |  | 
**source** | **str** |  | 
**year** | **int** |  | [optional] 
**fallback_reason** | **str** |  | [optional] 
**value** | **object** | The metric&#39;s raw typed value for this school/source | 
**comparability_state** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.financial_comparison_ranked_row import FinancialComparisonRankedRow

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialComparisonRankedRow from a JSON string
financial_comparison_ranked_row_instance = FinancialComparisonRankedRow.from_json(json)
# print the JSON string representation of the object
print(FinancialComparisonRankedRow.to_json())

# convert the object into a dict
financial_comparison_ranked_row_dict = financial_comparison_ranked_row_instance.to_dict()
# create an instance of FinancialComparisonRankedRow from a dict
financial_comparison_ranked_row_from_dict = FinancialComparisonRankedRow.from_dict(financial_comparison_ranked_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


