# EadaDerivedMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonical_metric_id** | **str** |  | 
**label** | **str** |  | 
**description** | **str** |  | [optional] 
**formula** | **str** |  | 
**source_service** | **str** |  | 

## Example

```python
from winthrop_client_python.models.eada_derived_metric import EadaDerivedMetric

# TODO update the JSON string below
json = "{}"
# create an instance of EadaDerivedMetric from a JSON string
eada_derived_metric_instance = EadaDerivedMetric.from_json(json)
# print the JSON string representation of the object
print(EadaDerivedMetric.to_json())

# convert the object into a dict
eada_derived_metric_dict = eada_derived_metric_instance.to_dict()
# create an instance of EadaDerivedMetric from a dict
eada_derived_metric_from_dict = EadaDerivedMetric.from_dict(eada_derived_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


