# GamePostSearchResultGamesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**neutral** | **bool** |  | [optional] 
**in_conference** | **bool** |  | [optional] 
**description** | **str** | Free-text game note (e.g. tournament name for neutral-site games) | [optional] 
**is_home** | **bool** | Whether the posting school is the home team | [optional] 
**opponent_id** | **int** |  | [optional] 
**opponent_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_games_inner import GamePostSearchResultGamesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultGamesInner from a JSON string
game_post_search_result_games_inner_instance = GamePostSearchResultGamesInner.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultGamesInner.to_json())

# convert the object into a dict
game_post_search_result_games_inner_dict = game_post_search_result_games_inner_instance.to_dict()
# create an instance of GamePostSearchResultGamesInner from a dict
game_post_search_result_games_inner_from_dict = GamePostSearchResultGamesInner.from_dict(game_post_search_result_games_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


