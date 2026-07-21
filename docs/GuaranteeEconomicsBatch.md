# GuaranteeEconomicsBatch

Batch guarantee economics (WINAD-10147) — the shared season window plus one entry per requested [school_id, sport_id] pair. Each pair's host/travel reuse GuaranteeEconomicsSide, so the same client view feeds GuaranteeChips whether it was singular- or batch-sourced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_window** | **str** | Identical for every pair (e.g. \&quot;last_3_completed_seasons\&quot;). | [optional] 
**seasons** | **List[int]** | Completed seasons behind the medians, ascending — shared across all pairs. | [optional] 
**pairs** | [**List[GuaranteeEconomicsBatchPair]**](GuaranteeEconomicsBatchPair.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_economics_batch import GuaranteeEconomicsBatch

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeEconomicsBatch from a JSON string
guarantee_economics_batch_instance = GuaranteeEconomicsBatch.from_json(json)
# print the JSON string representation of the object
print(GuaranteeEconomicsBatch.to_json())

# convert the object into a dict
guarantee_economics_batch_dict = guarantee_economics_batch_instance.to_dict()
# create an instance of GuaranteeEconomicsBatch from a dict
guarantee_economics_batch_from_dict = GuaranteeEconomicsBatch.from_dict(guarantee_economics_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


