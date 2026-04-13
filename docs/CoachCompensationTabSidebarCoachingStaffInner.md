# CoachCompensationTabSidebarCoachingStaffInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**coach_friendly_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**initials** | **str** |  | [optional] 
**position_types** | **List[str]** |  | [optional] 
**salary_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.coach_compensation_tab_sidebar_coaching_staff_inner import CoachCompensationTabSidebarCoachingStaffInner

# TODO update the JSON string below
json = "{}"
# create an instance of CoachCompensationTabSidebarCoachingStaffInner from a JSON string
coach_compensation_tab_sidebar_coaching_staff_inner_instance = CoachCompensationTabSidebarCoachingStaffInner.from_json(json)
# print the JSON string representation of the object
print(CoachCompensationTabSidebarCoachingStaffInner.to_json())

# convert the object into a dict
coach_compensation_tab_sidebar_coaching_staff_inner_dict = coach_compensation_tab_sidebar_coaching_staff_inner_instance.to_dict()
# create an instance of CoachCompensationTabSidebarCoachingStaffInner from a dict
coach_compensation_tab_sidebar_coaching_staff_inner_from_dict = CoachCompensationTabSidebarCoachingStaffInner.from_dict(coach_compensation_tab_sidebar_coaching_staff_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


