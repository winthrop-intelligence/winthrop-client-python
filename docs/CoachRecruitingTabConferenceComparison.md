# CoachRecruitingTabConferenceComparison


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**entries** | [**List[RecruitingConferenceEntry]**](RecruitingConferenceEntry.md) |  | 

## Example

```python
from winthrop_client_python.models.coach_recruiting_tab_conference_comparison import CoachRecruitingTabConferenceComparison

# TODO update the JSON string below
json = "{}"
# create an instance of CoachRecruitingTabConferenceComparison from a JSON string
coach_recruiting_tab_conference_comparison_instance = CoachRecruitingTabConferenceComparison.from_json(json)
# print the JSON string representation of the object
print(CoachRecruitingTabConferenceComparison.to_json())

# convert the object into a dict
coach_recruiting_tab_conference_comparison_dict = coach_recruiting_tab_conference_comparison_instance.to_dict()
# create an instance of CoachRecruitingTabConferenceComparison from a dict
coach_recruiting_tab_conference_comparison_from_dict = CoachRecruitingTabConferenceComparison.from_dict(coach_recruiting_tab_conference_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


