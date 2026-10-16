# FinancialComparisonRankings

Rankings for each supported financial source. A source is omitted when it has no matching rows. Explicit source properties keep each array's ranked-row decoder available to generated clients.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eada** | [**List[FinancialComparisonRankedRow]**](FinancialComparisonRankedRow.md) |  | [optional] 
**ncaa_frs** | [**List[FinancialComparisonRankedRow]**](FinancialComparisonRankedRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.financial_comparison_rankings import FinancialComparisonRankings

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialComparisonRankings from a JSON string
financial_comparison_rankings_instance = FinancialComparisonRankings.from_json(json)
# print the JSON string representation of the object
print(FinancialComparisonRankings.to_json())

# convert the object into a dict
financial_comparison_rankings_dict = financial_comparison_rankings_instance.to_dict()
# create an instance of FinancialComparisonRankings from a dict
financial_comparison_rankings_from_dict = FinancialComparisonRankings.from_dict(financial_comparison_rankings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


