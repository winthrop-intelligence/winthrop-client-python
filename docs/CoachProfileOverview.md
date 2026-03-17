# CoachProfileOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensations** | [**List[CoachCompensationEntry]**](CoachCompensationEntry.md) |  | 
**total_compensations** | **int** |  | 
**positions_by_sport** | **Dict[str, List[CoachPositionEntry]]** |  | 
**total_positions** | **int** |  | 
**conference_positions_by_sport** | **Dict[str, List[ConferencePositionEntry]]** |  | 
**snapshot** | [**CoachSnapshot**](CoachSnapshot.md) |  | [optional] 
**videos** | [**List[CoachVideoEntry]**](CoachVideoEntry.md) |  | 
**can_see_compensation** | **bool** |  | 
**can_see_videos** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.coach_profile_overview import CoachProfileOverview

# TODO update the JSON string below
json = "{}"
# create an instance of CoachProfileOverview from a JSON string
coach_profile_overview_instance = CoachProfileOverview.from_json(json)
# print the JSON string representation of the object
print(CoachProfileOverview.to_json())

# convert the object into a dict
coach_profile_overview_dict = coach_profile_overview_instance.to_dict()
# create an instance of CoachProfileOverview from a dict
coach_profile_overview_from_dict = CoachProfileOverview.from_dict(coach_profile_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


