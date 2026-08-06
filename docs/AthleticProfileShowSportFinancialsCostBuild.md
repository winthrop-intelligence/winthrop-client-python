# AthleticProfileShowSportFinancialsCostBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_coach** | [**AthleticProfileShowSportFinancialsCostBuildHeadCoach**](AthleticProfileShowSportFinancialsCostBuildHeadCoach.md) |  | [optional] 
**assistant_pool** | [**AthleticProfileShowSportFinancialsCostBuildAssistantPool**](AthleticProfileShowSportFinancialsCostBuildAssistantPool.md) |  | [optional] 
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


