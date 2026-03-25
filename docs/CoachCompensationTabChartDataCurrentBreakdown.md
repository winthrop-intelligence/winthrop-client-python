# CoachCompensationTabChartDataCurrentBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_salary_cents** | **int** |  | [optional] 
**talent_fee_cents** | **int** |  | [optional] 
**deferred_comp_cents** | **int** |  | [optional] 
**total_cents** | **int** |  | [optional] 
**year_str** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_chart_data_current_breakdown import CoachCompensationTabChartDataCurrentBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabChartDataCurrentBreakdown from a JSON string
coach_compensation_tab_chart_data_current_breakdown_instance = CoachCompensationTabChartDataCurrentBreakdown.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabChartDataCurrentBreakdown.to_json())

# convert the object into a dict
coach_compensation_tab_chart_data_current_breakdown_dict = coach_compensation_tab_chart_data_current_breakdown_instance.to_dict()
# create an instance of CoachCompensationTabChartDataCurrentBreakdown from a dict
coach_compensation_tab_chart_data_current_breakdown_from_dict = CoachCompensationTabChartDataCurrentBreakdown.from_dict(coach_compensation_tab_chart_data_current_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


