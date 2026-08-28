# EadaNormalizedMetric

One self-describing EADA metric — WINAD-10370's normalized shape, driven by the WINAD-10371 catalog (Eada::MetricCatalog).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**year** | **int** |  | 
**report_type** | **str** |  | 
**grain** | **str** |  | 
**family** | **str** |  | 
**metric** | **str** | canonical_metric_id when the catalog has one, else the column/source field name | 
**canonical_metric_id** | **str** |  | [optional] 
**source_field** | **str** | Raw EADA source_payload/CSV header this metric was read from | 
**label** | **str** |  | [optional] 
**definition** | **str** |  | [optional] 
**value** | **object** | Raw typed-column value (whole dollars for usd fields — not cents) | 
**unit** | **str** |  | 
**gender** | **str** |  | [optional] 
**comparability_state** | **str** |  | [optional] 
**ncaa_counterpart** | **str** |  | [optional] 
**mapping_status** | **str** | Institution grain — the report&#39;s own school match_status. Sport grain — the source sport code&#39;s Eada::SportMapping status (mapped/ambiguous/unmapped/unknown). | 
**sport_code** | **str** |  | [optional] 
**sport_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.eada_normalized_metric import EadaNormalizedMetric

# TODO update the JSON string below
json = "{}"
# create an instance of EadaNormalizedMetric from a JSON string
eada_normalized_metric_instance = EadaNormalizedMetric.from_json(json)
# print the JSON string representation of the object
print(EadaNormalizedMetric.to_json())

# convert the object into a dict
eada_normalized_metric_dict = eada_normalized_metric_instance.to_dict()
# create an instance of EadaNormalizedMetric from a dict
eada_normalized_metric_from_dict = EadaNormalizedMetric.from_dict(eada_normalized_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


