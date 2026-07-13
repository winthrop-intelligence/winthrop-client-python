# GamePostSearchResult

Enriched game post search result with school, location, and ranking data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | FilSportGamePost ID | [optional] 
**publish_group_id** | **UUID** | Identifies the publish (one \&quot;Post game wanted\&quot; action) this card represents. Shared by every post created in the same publish, so the grouped feed renders one card per publish. Null for legacy posts. | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**schedule_profile_eligible** | **bool** | WINAD-10097 - whether the posting school has a supported D1/D2 schedule profile. When false the card omits its \&quot;View school profile\&quot; / school-name links to /schedules/:sport/:school_id. | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date_display** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**city** | **str** |  | [optional] 
**state_name** | **str** |  | [optional] 
**last_rpi** | **int** | Most recent RPI ranking | [optional] 
**distance** | **float** | Distance in miles from user&#39;s school | [optional] 
**game_types_display** | **str** | Comma-separated list of game type names | [optional] 
**created_by_name** | **str** | Full name of the user who created the game post | [optional] 
**created_by_scheduling_phone** | **str** | Post creator&#39;s user-controlled scheduling phone (textable); null when unset | [optional] 
**created_by_scheduling_phone_dial** | **str** | Dial-ready form of the creator&#39;s scheduling phone for tel links | [optional] 
**avg_net_rank** | **int** | 5-year average NET ranking | [optional] 
**school_logo_url** | **str** | URL to school logo image (small variant) | [optional] 
**posts** | [**List[GamePostSearchResultPostsInner]**](GamePostSearchResultPostsInner.md) | The posting school&#39;s own active Games Wanted posts for this sport, one entry per post (each carrying its id). Present only when group_by_school&#x3D;true, where the feed is grouped one row per school so this aggregates every post for the school. The card collapses same-day posts into chips; the school+sport show page lists each. With post_details&#x3D;true each entry also carries the per-post detail fields below. | [optional] 
**games** | [**List[GamePostSearchResultGamesInner]**](GamePostSearchResultGamesInner.md) | Games already on the posting school&#39;s schedule for this sport, within the current scheduling-season window. Opponent fields are relative to the posting school. | [optional] 
**schedule_intents** | [**List[GamePostSearchResultScheduleIntentsInner]**](GamePostSearchResultScheduleIntentsInner.md) | The posting school+sport&#39;s schedule-intent (availability) markers within the current scheduling-season window, only present for sports the requesting schedule user is permitted to see. WINAD-10093: these drive the feed card&#39;s displayed dates (the card is grouped per publish, but its dates come from the school&#39;s durable availability calendar, so deleting or expiring one publish group never shrinks a sibling card&#39;s dates). The private \&quot;Pending\&quot; marker is stripped: a Pending-only cell is omitted and a mixed cell drops the Pending type. WINAD: OMITTED when q[defer_enrichment] is set (the dashboard feed) — the open windows are then deferred to POST /game_post_searches/enrichment alongside overlap and guarantee, so the whole availability bar reveals together. Present on the inline path (the show page&#39;s post_details response). | [optional] 
**overlap** | [**GamePostSearchResultOverlap**](GamePostSearchResultOverlap.md) |  | [optional] 
**contact** | [**GamePostSearchResultContact**](GamePostSearchResultContact.md) |  | [optional] 
**guarantee** | [**GamePostSearchResultGuarantee**](GamePostSearchResultGuarantee.md) |  | [optional] 
**contacts** | [**List[GamePostSearchResultContactsInner]**](GamePostSearchResultContactsInner.md) | School+sport scheduling contacts, shared across the school&#39;s posts. Present only with post_details&#x3D;true (the school+sport show page). | [optional] 

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


