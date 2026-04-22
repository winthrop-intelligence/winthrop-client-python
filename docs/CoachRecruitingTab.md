# CoachRecruitingTab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**leader_ad** | **bool** |  | 
**positions** | [**List[RecruitingPositionEntry]**](RecruitingPositionEntry.md) |  | 
**conference_comparison** | [**CoachRecruitingTabConferenceComparison**](CoachRecruitingTabConferenceComparison.md) |  | [optional] 
**can_see_financials** | **bool** |  | 
**recruiting_budgets** | [**CoachRecruitingTabRecruitingBudgets**](CoachRecruitingTabRecruitingBudgets.md) |  | [optional] 
**sport_budgets** | [**CoachRecruitingTabRecruitingBudgets**](CoachRecruitingTabRecruitingBudgets.md) |  | [optional] 
**chart_data** | [**RecruitingChartData**](RecruitingChartData.md) |  | [optional] 
**metadata** | [**CoachRecruitingTabMetadata**](CoachRecruitingTabMetadata.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_recruiting_tab import CoachRecruitingTab

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRecruitingTab from a JSON string
coach_recruiting_tab_instance = CoachRecruitingTab.from_json(json)
# print the JSON string representation of the object
print(CoachRecruitingTab.to_json())

# convert the object into a dict
coach_recruiting_tab_dict = coach_recruiting_tab_instance.to_dict()
# create an instance of CoachRecruitingTab from a dict
coach_recruiting_tab_from_dict = CoachRecruitingTab.from_dict(coach_recruiting_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


