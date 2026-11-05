# CreatePlayerStatRequestPlayerStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **int** |  | 
**school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**eligibility_year** | **int** |  | 
**eligible** | **str** |  | [optional] 
**recruit_year** | **bool** |  | [optional] 
**transfer_year** | **bool** |  | [optional] 
**last_season** | **bool** |  | [optional] 
**position** | **str** |  | [optional] 
**player_number** | **int** |  | [optional] 
**average_stars** | **float** |  | [optional] 
**overall_ranking** | **int** |  | [optional] 
**position_ranking** | **int** |  | [optional] 
**points** | **int** |  | [optional] 
**rebounds** | **int** |  | [optional] 
**assists** | **int** |  | [optional] 
**games** | **int** |  | [optional] 
**minutes** | **int** |  | [optional] 
**field_goals_made** | **int** |  | [optional] 
**field_goals_attempted** | **int** |  | [optional] 
**free_throws_made** | **int** |  | [optional] 
**free_throws_attempted** | **int** |  | [optional] 
**three_pointers_made** | **int** |  | [optional] 
**three_pointers_attempted** | **int** |  | [optional] 
**offensive_rebounds** | **int** |  | [optional] 
**defensive_rebounds** | **int** |  | [optional] 
**steals** | **int** |  | [optional] 
**blocks** | **int** |  | [optional] 
**turnovers** | **int** |  | [optional] 
**personal_fouls** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_player_stat_request_player_stat import CreatePlayerStatRequestPlayerStat

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlayerStatRequestPlayerStat from a JSON string
create_player_stat_request_player_stat_instance = CreatePlayerStatRequestPlayerStat.from_json(json)
# print the JSON string representation of the object
print(CreatePlayerStatRequestPlayerStat.to_json())

# convert the object into a dict
create_player_stat_request_player_stat_dict = create_player_stat_request_player_stat_instance.to_dict()
# create an instance of CreatePlayerStatRequestPlayerStat from a dict
create_player_stat_request_player_stat_from_dict = CreatePlayerStatRequestPlayerStat.from_dict(create_player_stat_request_player_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


