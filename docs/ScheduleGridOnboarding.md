# ScheduleGridOnboarding

Empty-schedule onboarding state for the logged-in school's upcoming schedule grid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show** | **bool** | True when the onboarding banner and + Add tooltip should be shown | [optional] 
**has_school_entered_content** | **bool** | True when the logged-in school has entered any own-schedule content for this sport and upcoming season | [optional] 
**suggested_schools** | [**List[ScheduleGridSchool]**](ScheduleGridSchool.md) | Top non-conference schools suggested as comparison columns for this sport and upcoming season | [optional] 

## Example

```python
from winthrop_client_python.models.schedule_grid_onboarding import ScheduleGridOnboarding

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleGridOnboarding from a JSON string
schedule_grid_onboarding_instance = ScheduleGridOnboarding.from_json(json)
# print the JSON string representation of the object
print(ScheduleGridOnboarding.to_json())

# convert the object into a dict
schedule_grid_onboarding_dict = schedule_grid_onboarding_instance.to_dict()
# create an instance of ScheduleGridOnboarding from a dict
schedule_grid_onboarding_from_dict = ScheduleGridOnboarding.from_dict(schedule_grid_onboarding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


