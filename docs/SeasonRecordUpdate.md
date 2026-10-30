# SeasonRecordUpdate

Only the fields in the body change; an explicit null clears a field. wins, losses and ties are the season totals: when regular_season_* and postseason_* are set they must add up to them (422). conference_position must not be larger than conference_num_positions. An optional change_note is stored on the audit version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**cfp_rank** | **int** |  | [optional] 
**torvik_rank** | **int** |  | [optional] 
**sos_ranking** | **int** |  | [optional] 
**non_conference_sos_ranking** | **int** |  | [optional] 
**conference_sos_ranking** | **int** |  | [optional] 
**recruit_ranking** | **int** |  | [optional] 
**attendance** | **int** |  | [optional] 
**regular_season_wins** | **int** |  | [optional] 
**regular_season_losses** | **int** |  | [optional] 
**regular_season_ties** | **int** |  | [optional] 
**postseason_wins** | **int** |  | [optional] 
**postseason_losses** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**sos** | **float** |  | [optional] 
**offensive_efficiency** | **float** |  | [optional] 
**defensive_efficiency** | **float** |  | [optional] 
**ranking_through_date** | **date** |  | [optional] 
**conference_regular_season_champion** | **bool** | null means unknown | [optional] 
**conference_tournament_champion** | **bool** | null means unknown | [optional] 
**change_note** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.season_record_update import SeasonRecordUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonRecordUpdate from a JSON string
season_record_update_instance = SeasonRecordUpdate.from_json(json)
# print the JSON string representation of the object
print(SeasonRecordUpdate.to_json())

# convert the object into a dict
season_record_update_dict = season_record_update_instance.to_dict()
# create an instance of SeasonRecordUpdate from a dict
season_record_update_from_dict = SeasonRecordUpdate.from_dict(season_record_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


