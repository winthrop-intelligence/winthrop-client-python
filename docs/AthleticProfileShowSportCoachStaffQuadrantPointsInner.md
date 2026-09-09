# AthleticProfileShowSportCoachStaffQuadrantPointsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**colors** | **str** |  | [optional] 
**is_subject** | **bool** |  | [optional] 
**coach_name** | **str** |  | [optional] 
**coach_last_name** | **str** | Structured last name — may be multi-word (\&quot;Hughley Jr\&quot;). | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_basis** | **str** | Which filing this dot&#39;s pay came from. A private peer files no coach contract, so it plots from its seat&#39;s IRS 990 line rather than going unplotted (WINAD-10406). The two filings measure different quantities — a 990 reports total compensation paid, a contract its guaranteed comp — so a 990 dot is plotted and labelled but stays out of every rank, median and verdict on the card. | [optional] 
**comp_fiscal_year** | **int** | The 990&#39;s own filing year; null for contract-basis dots. | [optional] 
**net_rank** | **int** |  | [optional] 
**rpi** | **int** |  | [optional] 
**conference_wins** | **int** |  | [optional] 
**record** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_coach_staff_quadrant_points_inner import AthleticProfileShowSportCoachStaffQuadrantPointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportCoachStaffQuadrantPointsInner from a JSON string
athletic_profile_show_sport_coach_staff_quadrant_points_inner_instance = AthleticProfileShowSportCoachStaffQuadrantPointsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportCoachStaffQuadrantPointsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_coach_staff_quadrant_points_inner_dict = athletic_profile_show_sport_coach_staff_quadrant_points_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportCoachStaffQuadrantPointsInner from a dict
athletic_profile_show_sport_coach_staff_quadrant_points_inner_from_dict = AthleticProfileShowSportCoachStaffQuadrantPointsInner.from_dict(athletic_profile_show_sport_coach_staff_quadrant_points_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


