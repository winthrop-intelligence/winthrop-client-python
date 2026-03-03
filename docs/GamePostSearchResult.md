# GamePostSearchResult

Enriched game post search result with school, location, and RPI data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_post_id** | **int** | Game post ID | [optional] 
**id** | **int** | FilSportGamePost ID | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**end_date_display** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**conference_id** | **int** |  | [optional] 
**conference_name** | **str** |  | [optional] 
**division_id** | **int** |  | [optional] 
**division_name** | **str** |  | [optional] 
**last_rpi** | **int** | Most recent RPI ranking | [optional] 
**distance** | **float** | Distance in miles from user&#39;s school | [optional] 
**avg_guarantee_paid** | **float** |  | [optional] 
**avg_guarantee_received** | **float** |  | [optional] 
**game_types_display** | **str** | Comma-separated list of game type names | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result import GamePostSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResult from a JSON string
game_post_search_result_instance = GamePostSearchResult.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResult.to_json())

# convert the object into a dict
game_post_search_result_dict = game_post_search_result_instance.to_dict()
# create an instance of GamePostSearchResult from a dict
game_post_search_result_from_dict = GamePostSearchResult.from_dict(game_post_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


