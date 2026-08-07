# AthleticProfileShowSportCoachStaffAssistantsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**last_name** | **str** | Structured last name — may be multi-word (\&quot;Hughley Jr\&quot;). | [optional] 
**title** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**contract_end_on** | **date** |  | [optional] 
**at_will** | **bool** | True when no term is stated (no contract, at-will contract, or no end date). Null when compensation is not permitted. | [optional] 
**on_file** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_sport_coach_staff_assistants_inner import AthleticProfileShowSportCoachStaffAssistantsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowSportCoachStaffAssistantsInner from a JSON string
athletic_profile_show_sport_coach_staff_assistants_inner_instance = AthleticProfileShowSportCoachStaffAssistantsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowSportCoachStaffAssistantsInner.to_json())

# convert the object into a dict
athletic_profile_show_sport_coach_staff_assistants_inner_dict = athletic_profile_show_sport_coach_staff_assistants_inner_instance.to_dict()
# create an instance of AthleticProfileShowSportCoachStaffAssistantsInner from a dict
athletic_profile_show_sport_coach_staff_assistants_inner_from_dict = AthleticProfileShowSportCoachStaffAssistantsInner.from_dict(athletic_profile_show_sport_coach_staff_assistants_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


