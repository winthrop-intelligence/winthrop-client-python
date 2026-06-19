# GamePostSearchResult

Enriched game post search result with school, location, and ranking data

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
**last_net_rank** | **int** | Most recent NET ranking | [optional] 
**last_ap_rank** | **int** | Most recent AP ranking | [optional] 
**distance** | **float** | Distance in miles from user&#39;s school | [optional] 
**avg_guarantee_paid** | **float** |  | [optional] 
**avg_guarantee_received** | **float** |  | [optional] 
**game_types_display** | **str** | Comma-separated list of game type names | [optional] 
**created_by_name** | **str** | Full name of the user who created the game post | [optional] 
**created_by_scheduling_phone** | **str** | Post creator&#39;s user-controlled scheduling phone (textable); null when unset | [optional] 
**created_by_scheduling_phone_dial** | **str** | Dial-ready form of the creator&#39;s scheduling phone for tel links | [optional] 
**avg_rpi** | **int** | 5-year average RPI ranking | [optional] 
**avg_net_rank** | **int** | 5-year average NET ranking | [optional] 
**avg_ap_rank** | **int** | 5-year average AP ranking | [optional] 
**school_logo_url** | **str** | URL to school logo image (small variant) | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**can_manage** | **bool** | Whether the current user can manage this game post | [optional] 
**posts** | [**List[GamePostSearchResultPostsInner]**](GamePostSearchResultPostsInner.md) | The posting school&#39;s own active Games Wanted posts for this sport, one entry per day (the card&#39;s date chips). Present only when group_by_school&#x3D;true, where the feed is grouped one row per school so this aggregates every post for the school. | [optional] 
**games** | [**List[GamePostSearchResultGamesInner]**](GamePostSearchResultGamesInner.md) | Games already on the posting school&#39;s schedule for this sport, within the current scheduling-season window. Opponent fields are relative to the posting school. | [optional] 
**schedule_intents** | [**List[GamePostSearchResultScheduleIntentsInner]**](GamePostSearchResultScheduleIntentsInner.md) | Private schedule-intent (requested availability) markers for the posting school and sport, within the current scheduling-season window. Only present for sports the requesting schedule user is permitted to see. | [optional] 

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


