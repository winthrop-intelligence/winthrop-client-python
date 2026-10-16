# AthleticProfileShowSportFinancialsCostBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_coach** | [**AthleticProfileShowSportFinancialsCostBuildHeadCoach**](AthleticProfileShowSportFinancialsCostBuildHeadCoach.md) |  | [optional] 
**game_day_operating** | [**AthleticProfileShowSportFinancialsCostBuildGameDayOperating**](AthleticProfileShowSportFinancialsCostBuildGameDayOperating.md) |  | [optional] 
**assistant_pool** | [**AthleticProfileShowSportFinancialsCostBuildAssistantPool**](AthleticProfileShowSportFinancialsCostBuildAssistantPool.md) |  | [optional] 
**head_coach_undisclosed** | [**AthleticProfileShowSportFinancialsCostBuildHeadCoachUndisclosed**](AthleticProfileShowSportFinancialsCostBuildHeadCoachUndisclosed.md) |  | [optional] 
**assistant_seats** | **int** | Private schools only — assistant seats the season&#39;s roster carries, priced by no filing (the 990 names no assistant). Null for a public school. | [optional] 
**guarantees_net** | [**AthleticProfileShowSportFinancialsCostBuildGuaranteesNet**](AthleticProfileShowSportFinancialsCostBuildGuaranteesNet.md) |  | [optional] 
**support_staff** | [**List[AthleticProfileShowSportFinancialsCostBuildSupportStaffInner]**](AthleticProfileShowSportFinancialsCostBuildSupportStaffInner.md) | Private schools only — support-staff compensation on record. Empty for a public school, whose support-staff line is read from the FRS filing (report_lines). | [optional] 
**report_lines** | [**List[AthleticProfileShowSportFinancialsCostBuildReportLinesInner]**](AthleticProfileShowSportFinancialsCostBuildReportLinesInner.md) | Public schools only — the program cost lines read from the sport&#39;s NCAA FRS filing for the selected season, in display order. Game expenses fall back to the EADA game-day operating expense when the FRS filing carries no split. A line the filing does not carry is absent; a filed zero is present. Empty for a private school. | [optional] 
**guarantees_received** | [**AthleticProfileShowSportFinancialsCostBuildGuaranteesReceived**](AthleticProfileShowSportFinancialsCostBuildGuaranteesReceived.md) |  | [optional] 
**total_cents** | **int** | A public total is the contract head coach plus every report line, stated only when every line is on the FRS filing; a private total sums the documented lines. Null otherwise — a partial sum is never stated. | [optional] 

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


