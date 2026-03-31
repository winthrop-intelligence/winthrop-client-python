# TeamScheduleOverlap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_overlap** | **bool** |  | [optional] 
**season_label** | **str** |  | [optional] 
**team_school_name** | **str** |  | [optional] 
**user_school_name** | **str** |  | [optional] 
**months** | **List[date]** |  | [optional] 
**team_games** | [**List[TeamScheduleOverlapTeamGamesInner]**](TeamScheduleOverlapTeamGamesInner.md) |  | [optional] 
**user_games** | [**List[TeamScheduleOverlapTeamGamesInner]**](TeamScheduleOverlapTeamGamesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_overlap import TeamScheduleOverlap

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleOverlap from a JSON string
team_schedule_overlap_instance = TeamScheduleOverlap.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleOverlap.to_json())

# convert the object into a dict
team_schedule_overlap_dict = team_schedule_overlap_instance.to_dict()
# create an instance of TeamScheduleOverlap from a dict
team_schedule_overlap_from_dict = TeamScheduleOverlap.from_dict(team_schedule_overlap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


