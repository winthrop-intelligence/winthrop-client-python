# GuaranteeBenchmarkError

Structured error returned in place of tier data when sport_id is missing, unknown, or not a basketball sport.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**suggested_fix** | **str** |  | [optional] 
**received_args** | **Dict[str, object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_benchmark_error import GuaranteeBenchmarkError

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeBenchmarkError from a JSON string
guarantee_benchmark_error_instance = GuaranteeBenchmarkError.from_json(json)
# print the JSON string representation of the object
print(GuaranteeBenchmarkError.to_json())

# convert the object into a dict
guarantee_benchmark_error_dict = guarantee_benchmark_error_instance.to_dict()
# create an instance of GuaranteeBenchmarkError from a dict
guarantee_benchmark_error_from_dict = GuaranteeBenchmarkError.from_dict(guarantee_benchmark_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


