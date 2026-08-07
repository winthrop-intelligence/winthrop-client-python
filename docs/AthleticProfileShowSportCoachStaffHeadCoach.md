# AthleticProfileShowSportCoachStaffHeadCoach


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**last_name** | **str** | Structured last name — may be multi-word (\&quot;Hughley Jr\&quot;). | [optional] 
**comp_cents** | **int** |  | [optional] 
**base_salary_cents** | **int** |  | [optional] 
**comp_rank** | **int** |  | [optional] 
**comp_cohort_size** | **int** |  | [optional] 
**comp_median_cents** | **int** |  | [optional] 
**contract_start_on** | **date** |  | [optional] 
**contract_end_on** | **date** |  | [optional] 
**contract_on_file** | **bool** |  | [optional] 
**at_will** | **bool** |  | [optional] 
**interim** | **bool** | True when the resolved seat-holder&#39;s position is interim-only. | [optional] 
**first_season_year** | **int** |  | [optional] 
**career_season_count** | **int** | Total recorded head-coach seasons across schools; career rows are capped at 12 selected seasons. | [optional] 
**year_one** | [**AthleticProfileShowSportCoachStaffHeadCoachYearOne**](AthleticProfileShowSportCoachStaffHeadCoachYearOne.md) |  | [optional] 
**career** | [**List[AthleticProfileShowSportCoachStaffHeadCoachCareerInner]**](AthleticProfileShowSportCoachStaffHeadCoachCareerInner.md) | Head-coach seasons across schools, most recent first, seasons with nothing filed under the active lens excluded, capped at 12. | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_coach_staff_head_coach import AthleticProfileShowSportCoachStaffHeadCoach

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportCoachStaffHeadCoach from a JSON string
athletic_profile_show_sport_coach_staff_head_coach_instance = AthleticProfileShowSportCoachStaffHeadCoach.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportCoachStaffHeadCoach.to_json())

# convert the object into a dict
athletic_profile_show_sport_coach_staff_head_coach_dict = athletic_profile_show_sport_coach_staff_head_coach_instance.to_dict()
# create an instance of AthleticProfileShowSportCoachStaffHeadCoach from a dict
athletic_profile_show_sport_coach_staff_head_coach_from_dict = AthleticProfileShowSportCoachStaffHeadCoach.from_dict(athletic_profile_show_sport_coach_staff_head_coach_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


