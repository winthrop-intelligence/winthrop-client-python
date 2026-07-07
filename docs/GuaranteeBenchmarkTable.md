# GuaranteeBenchmarkTable

NCAA guarantee benchmark table for one basketball sport, grouped by basketball conference tier (high_major / upper_mid_major / mid_major / low_major — WINAD-10023). When sport_id is missing/unknown/non-basketball the `error` block is returned instead of `tiers`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport** | [**GadSchoolSummarySport**](GadSchoolSummarySport.md) |  | [optional] 
**your_tier** | **str** | The viewer&#39;s own basketball tier, used to highlight a row. Null when the account has no school, no conference membership for the sport, or is independent. | [optional] 
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


