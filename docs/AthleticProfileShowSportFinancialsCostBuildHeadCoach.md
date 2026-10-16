# AthleticProfileShowSportFinancialsCostBuildHeadCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**last_name** | **str** | Structured last name — may be multi-word (\&quot;Hughley Jr\&quot;). | [optional] 
**comp_cents** | **int** |  | [optional] 
**on_file** | **bool** |  | [optional] 
**comp_basis** | **str** | Which filing the figure is read from — a contract, or the school&#39;s IRS 990 for a private school. | [optional] 
**comp_fiscal_year** | **int** | The 990&#39;s filing year; null for a contract figure. | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_financials_cost_build_head_coach import AthleticProfileShowSportFinancialsCostBuildHeadCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportFinancialsCostBuildHeadCoach from a JSON string
athletic_profile_show_sport_financials_cost_build_head_coach_instance = AthleticProfileShowSportFinancialsCostBuildHeadCoach.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportFinancialsCostBuildHeadCoach.to_json())

# convert the object into a dict
athletic_profile_show_sport_financials_cost_build_head_coach_dict = athletic_profile_show_sport_financials_cost_build_head_coach_instance.to_dict()
# create an instance of AthleticProfileShowSportFinancialsCostBuildHeadCoach from a dict
athletic_profile_show_sport_financials_cost_build_head_coach_from_dict = AthleticProfileShowSportFinancialsCostBuildHeadCoach.from_dict(athletic_profile_show_sport_financials_cost_build_head_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


