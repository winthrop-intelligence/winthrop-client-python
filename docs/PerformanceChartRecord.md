# PerformanceChartRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.performance_chart_record import PerformanceChartRecord

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceChartRecord from a JSON string
performance_chart_record_instance = PerformanceChartRecord.from_json(json)
# print the JSON string representation of the object
print(PerformanceChartRecord.to_json())

# convert the object into a dict
performance_chart_record_dict = performance_chart_record_instance.to_dict()
# create an instance of PerformanceChartRecord from a dict
performance_chart_record_from_dict = PerformanceChartRecord.from_dict(performance_chart_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


