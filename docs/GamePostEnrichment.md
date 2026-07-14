# GamePostEnrichment

WINAD: one row of the deferred per-card blocks returned by POST /game_post_searches/enrichment, keyed by [school_id, sport_id] so the client merges it onto every feed card sharing that pair. Shapes mirror GamePostSearchResult exactly (the feed omits overlap/guarantee/schedule_intents under q[defer_enrichment] and this endpoint fills them in a beat later).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school_id** | **int** |  | 
**sport_id** | **int** |  | 
**schedule_intents** | [**List[GamePostEnrichmentScheduleIntentsInner]**](GamePostEnrichmentScheduleIntentsInner.md) | The posting school+sport&#39;s schedule-intent (availability) markers within the current scheduling-season window (the card&#39;s \&quot;open windows\&quot;), only for sports the requesting schedule user is permitted to see. Same shape and source as GamePostSearchResult.schedule_intents; the private \&quot;Pending\&quot; marker is stripped (a Pending-only cell is omitted, a mixed cell drops the Pending type). | 
**overlap** | [**GamePostEnrichmentOverlap**](GamePostEnrichmentOverlap.md) |  | 
**guarantee** | [**GamePostEnrichmentGuarantee**](GamePostEnrichmentGuarantee.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_enrichment import GamePostEnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostEnrichment from a JSON string
game_post_enrichment_instance = GamePostEnrichment.from_json(json)
# print the JSON string representation of the object
print(GamePostEnrichment.to_json())

# convert the object into a dict
game_post_enrichment_dict = game_post_enrichment_instance.to_dict()
# create an instance of GamePostEnrichment from a dict
game_post_enrichment_from_dict = GamePostEnrichment.from_dict(game_post_enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


