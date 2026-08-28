# FinancialSelection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**source** | **str** | The requested mode (eada, ncaa_frs, best_available, or both) — not necessarily every result&#39;s actual resolved source; see each result&#39;s own source. | 
**grain** | **str** |  | 
**requested_year** | **int** |  | 
**results** | [**List[FinancialSelectionResult]**](FinancialSelectionResult.md) | One Result per source actually shown — one entry for eada/ncaa_frs/ best_available modes, up to two under both. | 

## Example

```python
from winthrop_client_python.models.financial_selection import FinancialSelection

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialSelection from a JSON string
financial_selection_instance = FinancialSelection.from_json(json)
# print the JSON string representation of the object
print(FinancialSelection.to_json())

# convert the object into a dict
financial_selection_dict = financial_selection_instance.to_dict()
# create an instance of FinancialSelection from a dict
financial_selection_from_dict = FinancialSelection.from_dict(financial_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


