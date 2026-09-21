# AthleticProfileShowSportFinancialsCostBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_coach** | [**AthleticProfileShowSportFinancialsCostBuildHeadCoach**](AthleticProfileShowSportFinancialsCostBuildHeadCoach.md) |  | [optional] 
**game_day_operating** | [**AthleticProfileShowSportFinancialsCostBuildGameDayOperating**](AthleticProfileShowSportFinancialsCostBuildGameDayOperating.md) |  | [optional] 
**assistant_pool** | [**AthleticProfileShowSportFinancialsCostBuildAssistantPool**](AthleticProfileShowSportFinancialsCostBuildAssistantPool.md) |  | [optional] 
**head_coach_undisclosed** | [**AthleticProfileShowSportFinancialsCostBuildHeadCoachUndisclosed**](AthleticProfileShowSportFinancialsCostBuildHeadCoachUndisclosed.md) |  | [optional] 
**assistant_seats** | **int** | Private schools only — assistant seats the season&#39;s roster carries, priced by no filing (the 990 names no assistant). Null for a public school, whose pool is priced in assistant_pool. | [optional] 
**guarantees_net** | [**AthleticProfileShowSportFinancialsCostBuildGuaranteesNet**](AthleticProfileShowSportFinancialsCostBuildGuaranteesNet.md) |  | [optional] 
**support_staff** | [**List[AthleticProfileShowSportFinancialsCostBuildSupportStaffInner]**](AthleticProfileShowSportFinancialsCostBuildSupportStaffInner.md) |  | [optional] 
**total_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_financials_cost_build import AthleticProfileShowSportFinancialsCostBuild

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportFinancialsCostBuild from a JSON string
athletic_profile_show_sport_financials_cost_build_instance = AthleticProfileShowSportFinancialsCostBuild.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportFinancialsCostBuild.to_json())

# convert the object into a dict
athletic_profile_show_sport_financials_cost_build_dict = athletic_profile_show_sport_financials_cost_build_instance.to_dict()
# create an instance of AthleticProfileShowSportFinancialsCostBuild from a dict
athletic_profile_show_sport_financials_cost_build_from_dict = AthleticProfileShowSportFinancialsCostBuild.from_dict(athletic_profile_show_sport_financials_cost_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


