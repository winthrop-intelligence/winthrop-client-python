# PerformanceChartCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**position** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**coach_friendly_id** | **str** |  | 

## Example

```python
from winthrop_client_python.models.performance_chart_coach import PerformanceChartCoach

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceChartCoach from a JSON string
performance_chart_coach_instance = PerformanceChartCoach.from_json(json)
# print the JSON string representation of the object
print(PerformanceChartCoach.to_json())

# convert the object into a dict
performance_chart_coach_dict = performance_chart_coach_instance.to_dict()
# create an instance of PerformanceChartCoach from a dict
performance_chart_coach_from_dict = PerformanceChartCoach.from_dict(performance_chart_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


