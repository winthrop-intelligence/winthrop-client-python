# GameDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | 
**game_date** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**neutral** | **bool** |  | [optional] 
**city** | **str** |  | [optional] 
**game_contract_id** | **int** |  | [optional] 
**state_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**in_conference** | **bool** |  | [optional] 
**season_year_tbd** | **int** |  | [optional] 
**home_school_score** | **int** |  | [optional] 
**away_school_score** | **int** |  | [optional] 
**overtime** | **int** |  | [optional] 
**season_year** | **int** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**home_school_net_rank** | **int** | Latest NET ranking for the home team, or null when not loaded yet | [optional] 
**away_school_net_rank** | **int** | Latest NET ranking for the away team, or null when not loaded yet | [optional] 
**home_school_sos_ranking** | **int** | Latest strength-of-schedule ranking for the home team, or null when not loaded yet | [optional] 
**away_school_sos_ranking** | **int** | Latest strength-of-schedule ranking for the away team, or null when not loaded yet | [optional] 
**rankings_season_year** | **int** | Season year the displayed NET/SOS rankings are from, or null when neither team has a ranked season | [optional] 
**game_contract** | [**GameDetailAllOfGameContract**](GameDetailAllOfGameContract.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_detail import GameDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GameDetail from a JSON string
game_detail_instance = GameDetail.from_json(json)
# print the JSON string representation of the object
print(GameDetail.to_json())

# convert the object into a dict
game_detail_dict = game_detail_instance.to_dict()
# create an instance of GameDetail from a dict
game_detail_from_dict = GameDetail.from_dict(game_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


