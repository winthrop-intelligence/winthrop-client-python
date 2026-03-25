# CoachCompensationTabChartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conference_name** | **str** |  | [optional] 
**total_comp_over_time** | [**List[CoachCompensationTabChartDataTotalCompOverTimeInner]**](CoachCompensationTabChartDataTotalCompOverTimeInner.md) |  | [optional] 
**conference_avg_over_time** | [**List[CoachCompensationTabChartDataConferenceAvgOverTimeInner]**](CoachCompensationTabChartDataConferenceAvgOverTimeInner.md) |  | [optional] 
**current_breakdown** | [**CoachCompensationTabChartDataCurrentBreakdown**](CoachCompensationTabChartDataCurrentBreakdown.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_chart_data import CoachCompensationTabChartData

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabChartData from a JSON string
coach_compensation_tab_chart_data_instance = CoachCompensationTabChartData.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabChartData.to_json())

# convert the object into a dict
coach_compensation_tab_chart_data_dict = coach_compensation_tab_chart_data_instance.to_dict()
# create an instance of CoachCompensationTabChartData from a dict
coach_compensation_tab_chart_data_from_dict = CoachCompensationTabChartData.from_dict(coach_compensation_tab_chart_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


