# RecruitingChartData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**years** | **List[int]** |  | 
**recruit_rankings** | **List[int]** |  | 
**conf_recruit_rankings** | **List[float]** |  | 
**recruiting_budgets_dollars** | **List[float]** |  | 
**conf_recruiting_budgets_dollars** | **List[float]** |  | 
**sport_budgets_dollars** | **List[float]** |  | 
**conf_sport_budgets_dollars** | **List[float]** |  | 

## Example

```python
from winthrop_client_python.models.recruiting_chart_data import RecruitingChartData

# TODO update the JSON string below
json = "{}"
# create an instance of RecruitingChartData from a JSON string
recruiting_chart_data_instance = RecruitingChartData.from_json(json)
# print the JSON string representation of the object
print(RecruitingChartData.to_json())

# convert the object into a dict
recruiting_chart_data_dict = recruiting_chart_data_instance.to_dict()
# create an instance of RecruitingChartData from a dict
recruiting_chart_data_from_dict = RecruitingChartData.from_dict(recruiting_chart_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


