# UpdateAdminSeasonStatsRequestSeason

Any subset of the editable season stat fields, as strings; an empty string clears the value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**wins** | **str** |  | [optional] 
**losses** | **str** |  | [optional] 
**ties** | **str** |  | [optional] 
**conference_wins** | **str** |  | [optional] 
**conference_losses** | **str** |  | [optional] 
**conference_ties** | **str** |  | [optional] 
**conference_position** | **str** |  | [optional] 
**conference_num_positions** | **str** |  | [optional] 
**home_wins** | **str** |  | [optional] 
**home_losses** | **str** |  | [optional] 
**away_wins** | **str** |  | [optional] 
**away_losses** | **str** |  | [optional] 
**neutral_wins** | **str** |  | [optional] 
**neutral_losses** | **str** |  | [optional] 
**non_division_wins** | **str** |  | [optional] 
**non_division_losses** | **str** |  | [optional] 
**asr** | **str** |  | [optional] 
**apr** | **str** |  | [optional] 
**coach_apr** | **str** |  | [optional] 
**rpi** | **str** |  | [optional] 
**prev_rpi** | **str** |  | [optional] 
**net_rank** | **str** |  | [optional] 
**prev_net_rank** | **str** |  | [optional] 
**ap_rank** | **str** |  | [optional] 
**prev_ap_rank** | **str** |  | [optional] 
**torvik_rank** | **str** |  | [optional] 
**sos** | **str** |  | [optional] 
**sos_ranking** | **str** |  | [optional] 
**non_conference_sos_ranking** | **str** |  | [optional] 
**conference_sos_ranking** | **str** |  | [optional] 
**ranking_through_date** | **str** |  | [optional] 
**attendance** | **str** |  | [optional] 
**recruit_ranking** | **str** |  | [optional] 
**offensive_efficiency** | **str** |  | [optional] 
**defensive_efficiency** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_season_stats_request_season import UpdateAdminSeasonStatsRequestSeason

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminSeasonStatsRequestSeason from a JSON string
update_admin_season_stats_request_season_instance = UpdateAdminSeasonStatsRequestSeason.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminSeasonStatsRequestSeason.to_json())

# convert the object into a dict
update_admin_season_stats_request_season_dict = update_admin_season_stats_request_season_instance.to_dict()
# create an instance of UpdateAdminSeasonStatsRequestSeason from a dict
update_admin_season_stats_request_season_from_dict = UpdateAdminSeasonStatsRequestSeason.from_dict(update_admin_season_stats_request_season_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


