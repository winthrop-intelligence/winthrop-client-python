# AdminSeasonStatsEditorSeason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**wins** | **int** |  | [optional] 
**losses** | **int** |  | [optional] 
**ties** | **int** |  | [optional] 
**conference_wins** | **int** |  | [optional] 
**conference_losses** | **int** |  | [optional] 
**conference_ties** | **int** |  | [optional] 
**conference_position** | **int** |  | [optional] 
**conference_num_positions** | **int** |  | [optional] 
**home_wins** | **int** |  | [optional] 
**home_losses** | **int** |  | [optional] 
**away_wins** | **int** |  | [optional] 
**away_losses** | **int** |  | [optional] 
**neutral_wins** | **int** |  | [optional] 
**neutral_losses** | **int** |  | [optional] 
**non_division_wins** | **int** |  | [optional] 
**non_division_losses** | **int** |  | [optional] 
**asr** | **int** |  | [optional] 
**apr** | **int** |  | [optional] 
**coach_apr** | **int** |  | [optional] 
**rpi** | **int** |  | [optional] 
**prev_rpi** | **int** |  | [optional] 
**net_rank** | **int** |  | [optional] 
**prev_net_rank** | **int** |  | [optional] 
**ap_rank** | **int** |  | [optional] 
**prev_ap_rank** | **int** |  | [optional] 
**torvik_rank** | **int** |  | [optional] 
**sos** | **str** | Decimal serialized as a string | [optional] 
**sos_ranking** | **int** |  | [optional] 
**non_conference_sos_ranking** | **int** |  | [optional] 
**conference_sos_ranking** | **int** |  | [optional] 
**ranking_through_date** | **date** | ISO 8601 calendar date (YYYY-MM-DD) | [optional] 
**attendance** | **int** |  | [optional] 
**recruit_ranking** | **int** |  | [optional] 
**offensive_efficiency** | **str** | Decimal serialized as a string | [optional] 
**defensive_efficiency** | **str** | Decimal serialized as a string | [optional] 

## Example

```python
from winthrop_client_python.models.admin_season_stats_editor_season import AdminSeasonStatsEditorSeason

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSeasonStatsEditorSeason from a JSON string
admin_season_stats_editor_season_instance = AdminSeasonStatsEditorSeason.from_json(json)
# print the JSON string representation of the object
print(AdminSeasonStatsEditorSeason.to_json())

# convert the object into a dict
admin_season_stats_editor_season_dict = admin_season_stats_editor_season_instance.to_dict()
# create an instance of AdminSeasonStatsEditorSeason from a dict
admin_season_stats_editor_season_from_dict = AdminSeasonStatsEditorSeason.from_dict(admin_season_stats_editor_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


