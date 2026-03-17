# PerformanceChartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | **List[str]** |  | 
**records** | [**List[PerformanceChartRecord]**](PerformanceChartRecord.md) |  | 
**coaches** | [**List[PerformanceChartCoach]**](PerformanceChartCoach.md) |  | 

## Example

```python
from winthrop_client_python.models.performance_chart_data import PerformanceChartData

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceChartData from a JSON string
performance_chart_data_instance = PerformanceChartData.from_json(json)
# print the JSON string representation of the object
print(PerformanceChartData.to_json())

# convert the object into a dict
performance_chart_data_dict = performance_chart_data_instance.to_dict()
# create an instance of PerformanceChartData from a dict
performance_chart_data_from_dict = PerformanceChartData.from_dict(performance_chart_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


