# AthleticProfileShowSportOverviewPayLadderInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_name** | **str** |  | [optional] 
**coach_last_name** | **str** | Structured last name — may be multi-word (\&quot;Hughley Jr\&quot;). | [optional] 
**school_short_name** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**is_subject** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_overview_pay_ladder_inner import AthleticProfileShowSportOverviewPayLadderInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportOverviewPayLadderInner from a JSON string
athletic_profile_show_sport_overview_pay_ladder_inner_instance = AthleticProfileShowSportOverviewPayLadderInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportOverviewPayLadderInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_overview_pay_ladder_inner_dict = athletic_profile_show_sport_overview_pay_ladder_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportOverviewPayLadderInner from a dict
athletic_profile_show_sport_overview_pay_ladder_inner_from_dict = AthleticProfileShowSportOverviewPayLadderInner.from_dict(athletic_profile_show_sport_overview_pay_ladder_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


