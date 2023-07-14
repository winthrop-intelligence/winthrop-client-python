# Game


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**home_school_id** | **int** |  | 
**away_school_id** | **int** |  | 
**sport_id** | **int** |  | 
**game_date** | **datetime** |  | 
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

## Example

```python
from winthrop_client_python.models.game import Game

# TODO update the JSON string below
json = "{}"
# create an instance of Game from a JSON string
game_instance = Game.from_json(json)
# print the JSON string representation of the object
print Game.to_json()

# convert the object into a dict
game_dict = game_instance.to_dict()
# create an instance of Game from a dict
game_form_dict = game.from_dict(game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


