# AthleticProfileShowSportCoachStaff

Coach & Staff tab payload for a sport scope; null for ADMIN scope. Compensation fields are null (never zero) when unfiled or not permitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_year** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**results_lens** | **str** | The ranking this sport is read through — NET for basketball, RPI for every other sport. Rank fields ship for both metrics; the lens names the one a surface may claim. | [optional] 
**quadrant_points** | [**List[AthleticProfileShowSportCoachStaffQuadrantPointsInner]**](AthleticProfileShowSportCoachStaffQuadrantPointsInner.md) | One entry per cohort school — head-coach pay vs the sport&#39;s results rank. | [optional] 
**head_coach** | [**AthleticProfileShowSportCoachStaffHeadCoach**](AthleticProfileShowSportCoachStaffHeadCoach.md) |  | [optional] 
**assistants** | [**List[AthleticProfileShowSportCoachStaffAssistantsInner]**](AthleticProfileShowSportCoachStaffAssistantsInner.md) |  | [optional] 
**staff_pool** | [**AthleticProfileShowSportCoachStaffStaffPool**](AthleticProfileShowSportCoachStaffStaffPool.md) |  | [optional] 
**support_staff** | [**List[AthleticProfileShowSportCoachStaffSupportStaffInner]**](AthleticProfileShowSportCoachStaffSupportStaffInner.md) | ALL_STAFF-group positions on file for the anchor season. No market-rate field — no data source. | [optional] 
**as_of** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_coach_staff import AthleticProfileShowSportCoachStaff

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportCoachStaff from a JSON string
athletic_profile_show_sport_coach_staff_instance = AthleticProfileShowSportCoachStaff.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportCoachStaff.to_json())

# convert the object into a dict
athletic_profile_show_sport_coach_staff_dict = athletic_profile_show_sport_coach_staff_instance.to_dict()
# create an instance of AthleticProfileShowSportCoachStaff from a dict
athletic_profile_show_sport_coach_staff_from_dict = AthleticProfileShowSportCoachStaff.from_dict(athletic_profile_show_sport_coach_staff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


