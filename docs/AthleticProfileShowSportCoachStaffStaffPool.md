# AthleticProfileShowSportCoachStaffStaffPool

Assistant pool vs the cohort; null when compensation is not permitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool_cents** | **int** |  | [optional] 
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


