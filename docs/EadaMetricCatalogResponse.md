# EadaMetricCatalogResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**catalog_version** | **int** |  | 
**data** | [**List[EadaMetricCatalogEntry]**](EadaMetricCatalogEntry.md) |  | 
**derived_metrics** | [**List[EadaDerivedMetric]**](EadaDerivedMetric.md) |  | 

## Example

```python
from winthrop_client_python.models.eada_metric_catalog_response import EadaMetricCatalogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EadaMetricCatalogResponse from a JSON string
eada_metric_catalog_response_instance = EadaMetricCatalogResponse.from_json(json)
# print the JSON string representation of the object
print(EadaMetricCatalogResponse.to_json())

# convert the object into a dict
eada_metric_catalog_response_dict = eada_metric_catalog_response_instance.to_dict()
# create an instance of EadaMetricCatalogResponse from a dict
eada_metric_catalog_response_from_dict = EadaMetricCatalogResponse.from_dict(eada_metric_catalog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


