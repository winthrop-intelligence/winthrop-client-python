# CoachCompensationTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_see_compensation** | **bool** |  | 
**chart_data** | [**CoachCompensationTabChartData**](CoachCompensationTabChartData.md) |  | [optional] 
**compensations** | [**List[CoachCompensationTabCompensationsInner]**](CoachCompensationTabCompensationsInner.md) |  | 
**total_compensations** | **int** |  | 
**comparisons** | [**CoachCompensationTabComparisons**](CoachCompensationTabComparisons.md) |  | [optional] 
**sidebar** | [**CoachCompensationTabSidebar**](CoachCompensationTabSidebar.md) |  | [optional] 
**quartiles** | [**QuartilesData**](QuartilesData.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab import CoachCompensationTab

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTab from a JSON string
coach_compensation_tab_instance = CoachCompensationTab.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTab.to_json())

# convert the object into a dict
coach_compensation_tab_dict = coach_compensation_tab_instance.to_dict()
# create an instance of CoachCompensationTab from a dict
coach_compensation_tab_from_dict = CoachCompensationTab.from_dict(coach_compensation_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


