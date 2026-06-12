# GuaranteeBenchmarkStats

Median / mean / min / max / count of comp_cents for one side of one tier, excluding comp_tbd=true agreements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**median_cents** | **int** |  | [optional] 
**mean_cents** | **int** |  | [optional] 
**min_cents** | **int** |  | [optional] 
**max_cents** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_benchmark_stats import GuaranteeBenchmarkStats

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeBenchmarkStats from a JSON string
guarantee_benchmark_stats_instance = GuaranteeBenchmarkStats.from_json(json)
# print the JSON string representation of the object
print(GuaranteeBenchmarkStats.to_json())

# convert the object into a dict
guarantee_benchmark_stats_dict = guarantee_benchmark_stats_instance.to_dict()
# create an instance of GuaranteeBenchmarkStats from a dict
guarantee_benchmark_stats_from_dict = GuaranteeBenchmarkStats.from_dict(guarantee_benchmark_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


