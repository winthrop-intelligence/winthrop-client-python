# FinancialComparison

Only present when metric was given. blended_ranking combines every source's values into one ranked list, but only when Financials::Comparability marks this canonical metric catalog-approved (comparability_state mergeable) for cross-source blending — no dollar-valued metric is mergeable in the catalog today, so blended_ranking is null with a blended_reason for every current financial metric. ranking_by_source is always populated — one ranking per source, kept visibly separate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric** | **str** |  | 
**mergeable_across_sources** | **bool** |  | 
**blended_ranking** | [**List[FinancialComparisonRankedRow]**](FinancialComparisonRankedRow.md) |  | [optional] 
**blended_reason** | **str** | Present only when blended_ranking is null — why this metric was not blended across sources. | [optional] 
**ranking_by_source** | **Dict[str, List[FinancialComparisonRankedRow]]** | One key per source that produced at least one matching row (e.g. eada, ncaa_frs), each an array of ranked rows for that source alone. | 

## Example

```python
from winthrop_client_python.models.financial_comparison import FinancialComparison

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialComparison from a JSON string
financial_comparison_instance = FinancialComparison.from_json(json)
# print the JSON string representation of the object
print(FinancialComparison.to_json())

# convert the object into a dict
financial_comparison_dict = financial_comparison_instance.to_dict()
# create an instance of FinancialComparison from a dict
financial_comparison_from_dict = FinancialComparison.from_dict(financial_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


