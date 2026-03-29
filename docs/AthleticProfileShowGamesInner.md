# AthleticProfileShowGamesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**opponent_name** | **str** |  | [optional] 
**opponent_id** | **int** |  | [optional] 
**is_away** | **bool** |  | [optional] 
**game_date** | **str** |  | [optional] 
**season_year_tbd** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**rpi** | **str** |  | [optional] 
**compensation_cents** | **int** |  | [optional] 
**game_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_games_inner import AthleticProfileShowGamesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowGamesInner from a JSON string
athletic_profile_show_games_inner_instance = AthleticProfileShowGamesInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowGamesInner.to_json())

# convert the object into a dict
athletic_profile_show_games_inner_dict = athletic_profile_show_games_inner_instance.to_dict()
# create an instance of AthleticProfileShowGamesInner from a dict
athletic_profile_show_games_inner_from_dict = AthleticProfileShowGamesInner.from_dict(athletic_profile_show_games_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


