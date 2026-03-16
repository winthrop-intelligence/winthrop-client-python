# TeamScheduleDetailSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**record_str** | **str** |  | [optional] 
**rpi** | **int** |  | [optional] 
**avg_rpi** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.team_schedule_detail_season import TeamScheduleDetailSeason

# TODO update the JSON string below
json = "{}"
# create an instance of TeamScheduleDetailSeason from a JSON string
team_schedule_detail_season_instance = TeamScheduleDetailSeason.from_json(json)
# print the JSON string representation of the object
print(TeamScheduleDetailSeason.to_json())

# convert the object into a dict
team_schedule_detail_season_dict = team_schedule_detail_season_instance.to_dict()
# create an instance of TeamScheduleDetailSeason from a dict
team_schedule_detail_season_from_dict = TeamScheduleDetailSeason.from_dict(team_schedule_detail_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


