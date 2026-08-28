# FinancialSelectionMetric

WINAD-10369's shared self-describing metric shape (Financials::Metric) — the one row shape returned regardless of whether it came from EADA or NCAA/FRS, each carrying its own source and year so a consumer that flattens results across sources never loses provenance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**year** | **int** |  | 
**grain** | **str** |  | 
**canonical_metric_id** | **str** | The shared cross-source id when one exists (currently total_revenue, total_expenses). Never an invitation to sum or average two sources&#39; values for the same id — see comparability_state. | [optional] 
**native_metric_id** | **str** | The source&#39;s own metric id — identical to canonical_metric_id for NCAA/FRS lines, the EADA-native field name (e.g. exp_men) for EADA metrics translated onto the shared vocabulary at sport grain. | 
**label** | **str** |  | [optional] 
**value** | **object** | Raw typed value (whole dollars for usd fields — not cents) | [optional] 
**unit** | **str** |  | [optional] 
**comparability_state** | **str** |  | [optional] 
**counterpart_note** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**mapping_status** | **str** | \&quot;native\&quot; for NCAA/FRS lines; the EADA report/sport match status for EADA lines. | 
**sport_code** | **str** |  | [optional] 
**sport_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.financial_selection_metric import FinancialSelectionMetric

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialSelectionMetric from a JSON string
financial_selection_metric_instance = FinancialSelectionMetric.from_json(json)
# print the JSON string representation of the object
print(FinancialSelectionMetric.to_json())

# convert the object into a dict
financial_selection_metric_dict = financial_selection_metric_instance.to_dict()
# create an instance of FinancialSelectionMetric from a dict
financial_selection_metric_from_dict = FinancialSelectionMetric.from_dict(financial_selection_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


