# EadaMetricCatalogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_key** | **str** |  | 
**report_type** | **str** |  | 
**label** | **str** |  | 
**description** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**unit** | **str** |  | 
**reporting_grain** | **str** |  | 
**gender_dimension** | **str** |  | [optional] 
**null_zero_semantics** | **str** |  | [optional] 
**source_section** | **str** |  | [optional] 
**canonical_metric_id** | **str** |  | [optional] 
**supported_aggregations** | **List[str]** |  | [optional] 
**ncaa_counterpart** | **str** |  | [optional] 
**comparability_state** | **str** |  | [optional] 
**rationale** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.eada_metric_catalog_entry import EadaMetricCatalogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EadaMetricCatalogEntry from a JSON string
eada_metric_catalog_entry_instance = EadaMetricCatalogEntry.from_json(json)
# print the JSON string representation of the object
print(EadaMetricCatalogEntry.to_json())

# convert the object into a dict
eada_metric_catalog_entry_dict = eada_metric_catalog_entry_instance.to_dict()
# create an instance of EadaMetricCatalogEntry from a dict
eada_metric_catalog_entry_from_dict = EadaMetricCatalogEntry.from_dict(eada_metric_catalog_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


