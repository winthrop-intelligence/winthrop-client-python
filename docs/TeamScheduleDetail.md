# TeamScheduleDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**TeamScheduleDetailSchool**](TeamScheduleDetailSchool.md) |  | [optional] 
**sport** | [**ContactSearchCoachOptionsSportsInner**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 
**season_year** | **int** |  | [optional] 
**performance_year** | **int** |  | [optional] 
**season** | [**TeamScheduleDetailSeason**](TeamScheduleDetailSeason.md) |  | [optional] 
**head_coach** | [**TeamScheduleDetailHeadCoach**](TeamScheduleDetailHeadCoach.md) |  | [optional] 
**non_conf_games_count** | **int** |  | [optional] 
**fil_team_id** | **str** |  | [optional] 
**available_years** | **List[int]** |  | [optional] 
**contacts** | [**List[TeamScheduleContact]**](TeamScheduleContact.md) |  | [optional] 
**games** | [**List[TeamScheduleDetailGame]**](TeamScheduleDetailGame.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_detail import TeamScheduleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleDetail from a JSON string
team_schedule_detail_instance = TeamScheduleDetail.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleDetail.to_json())

# convert the object into a dict
team_schedule_detail_dict = team_schedule_detail_instance.to_dict()
# create an instance of TeamScheduleDetail from a dict
team_schedule_detail_from_dict = TeamScheduleDetail.from_dict(team_schedule_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


