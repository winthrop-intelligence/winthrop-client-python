# AthleticProfileShowSportCoachStaffStaffPool

Assistant pool vs the conference cohort, on one basis for every school. FRS assistant coaching totals (EXP_ASSISTANT_COACHES plus third party) when the subject and every cohort school filed them for the season; otherwise complete contract pools (every assistant priced, WINAD-10443) when every school has one. Null when no basis covers every school — the comparison is never shown over partial or mixed pools (WINAD-10444) — and for a private school.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_cents** | **int** |  | [optional] 
**basis** | **str** | The reporting basis every pool in the comparison shares. | [optional] 
**fiscal_year** | **int** | The FRS filing year; null for contract pools. | [optional] 
**cohort_size** | **int** |  | [optional] 
**cohort_rank** | **int** |  | [optional] 
**median_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_coach_staff_staff_pool import AthleticProfileShowSportCoachStaffStaffPool

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportCoachStaffStaffPool from a JSON string
athletic_profile_show_sport_coach_staff_staff_pool_instance = AthleticProfileShowSportCoachStaffStaffPool.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportCoachStaffStaffPool.to_json())

# convert the object into a dict
athletic_profile_show_sport_coach_staff_staff_pool_dict = athletic_profile_show_sport_coach_staff_staff_pool_instance.to_dict()
# create an instance of AthleticProfileShowSportCoachStaffStaffPool from a dict
athletic_profile_show_sport_coach_staff_staff_pool_from_dict = AthleticProfileShowSportCoachStaffStaffPool.from_dict(athletic_profile_show_sport_coach_staff_staff_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


