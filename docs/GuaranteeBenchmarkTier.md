# GuaranteeBenchmarkTier

Per-tier guarantee benchmark. paid_out aggregates contracts where the tier is the home/buyer side; received where it is the away/seller side.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tier** | **str** |  | [optional] 
**paid_out** | [**GuaranteeBenchmarkStats**](GuaranteeBenchmarkStats.md) |  | [optional] 
**received** | [**GuaranteeBenchmarkStats**](GuaranteeBenchmarkStats.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_benchmark_tier import GuaranteeBenchmarkTier

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeBenchmarkTier from a JSON string
guarantee_benchmark_tier_instance = GuaranteeBenchmarkTier.from_json(json)
# print the JSON string representation of the object
print(GuaranteeBenchmarkTier.to_json())

# convert the object into a dict
guarantee_benchmark_tier_dict = guarantee_benchmark_tier_instance.to_dict()
# create an instance of GuaranteeBenchmarkTier from a dict
guarantee_benchmark_tier_from_dict = GuaranteeBenchmarkTier.from_dict(guarantee_benchmark_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


