# FinancialSelectionResult

One source's resolved report for the requested school/grain/year (Financials::SourceSelection::Result) — never a row assembled from unrelated line items across two reports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**year** | **int** |  | [optional] 
**grain** | **str** |  | 
**available** | **bool** | False when no report exists for this source/year/grain, the report exists but has nothing actually reported (NCAA/FRS only), no sport-code crosswalk exists for this sport (EADA sport grain only), a requested metric filter matched nothing this source&#39;s vocabulary emits at all, or (single-source mode only) the viewer lacks the ability for this source on this school. | 
**fallback_reason** | **str** | sport_not_mapped_to_eada marks a WinAD sport with no EADA crosswalk row at all (a mapping gap, not a missing filing); source_not_permitted_for_viewer also covers best_available/both requests where the viewer holds neither source ability for this school. ncaa_frs_suppressed_private_school marks the NCAA FRS result for a private school — suppressed by policy for every viewer, whatever legacy data exists; the three *_used_eada reasons distinguish WHY best_available is showing EADA (no filing / viewer permission / private-school policy) so the UI never claims a filing gap when the truth is suppression. | [optional] 
**comparability_summary** | **str** | Most-conservative comparability_state across this result&#39;s metrics (not_comparable outranks comparison_only outranks mergeable; source_only is the fallback default). | 
**metrics** | [**List[FinancialSelectionMetric]**](FinancialSelectionMetric.md) |  | 

## Example

```python
from winthrop_client_python.models.financial_selection_result import FinancialSelectionResult

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialSelectionResult from a JSON string
financial_selection_result_instance = FinancialSelectionResult.from_json(json)
# print the JSON string representation of the object
print(FinancialSelectionResult.to_json())

# convert the object into a dict
financial_selection_result_dict = financial_selection_result_instance.to_dict()
# create an instance of FinancialSelectionResult from a dict
financial_selection_result_from_dict = FinancialSelectionResult.from_dict(financial_selection_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


