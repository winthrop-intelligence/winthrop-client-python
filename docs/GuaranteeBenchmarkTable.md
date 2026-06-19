# GuaranteeBenchmarkTable

NCAA guarantee benchmark table for one sport, reusing the Find Opponent \"Opponent Quality\" tiers (power_4 / mid_major / smaller). When sport_id is missing/unknown the `error` block is returned instead of `tiers`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | [**GadSchoolSummarySport**](GadSchoolSummarySport.md) |  | [optional] 
**your_tier** | **str** | The viewer&#39;s own tier, used to highlight a row. Null when the account has no school. | [optional] 
**season_window** | **str** |  | [optional] 
**seasons** | **List[int]** |  | [optional] 
**tiers** | [**List[GuaranteeBenchmarkTier]**](GuaranteeBenchmarkTier.md) |  | [optional] 
**error** | [**GuaranteeBenchmarkError**](GuaranteeBenchmarkError.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.guarantee_benchmark_table import GuaranteeBenchmarkTable

# TODO update the JSON string below
json = "{}"
# create an instance of GuaranteeBenchmarkTable from a JSON string
guarantee_benchmark_table_instance = GuaranteeBenchmarkTable.from_json(json)
# print the JSON string representation of the object
print(GuaranteeBenchmarkTable.to_json())

# convert the object into a dict
guarantee_benchmark_table_dict = guarantee_benchmark_table_instance.to_dict()
# create an instance of GuaranteeBenchmarkTable from a dict
guarantee_benchmark_table_from_dict = GuaranteeBenchmarkTable.from_dict(guarantee_benchmark_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


