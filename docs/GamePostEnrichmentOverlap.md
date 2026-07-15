# GamePostEnrichmentOverlap

Availability overlap between the requesting viewer's own school and this posting school for the sport (AvailabilityOverlapMatcher). Same shape as GamePostSearchResult.overlap: when the viewer has no school or no dates line up, total is 0 with an empty line_ups array (the no-overlap state).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of dates that line up on both sides. | 
**strong_count** | **int** | How many lined-up dates are strong (any actionable classification: guarantee, home_and_home, any_format, mte, or neutral_site). | 
**rollup_text** | **str** | Ready-made pill summary, e.g. \&quot;3 dates line up · 2 strong\&quot;. Null when there is no overlap (total 0). | [optional] 
**line_ups** | [**List[GamePostEnrichmentOverlapLineUpsInner]**](GamePostEnrichmentOverlapLineUpsInner.md) | One entry per lined-up date, strong (guarantee, home-and-home, any_format, mte, neutral_site) before possible, each tier ordered by ascending date. | 

## Example

```python
from winthrop_client_python.models.game_post_enrichment_overlap import GamePostEnrichmentOverlap

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostEnrichmentOverlap from a JSON string
game_post_enrichment_overlap_instance = GamePostEnrichmentOverlap.from_json(json)
# print the JSON string representation of the object
print(GamePostEnrichmentOverlap.to_json())

# convert the object into a dict
game_post_enrichment_overlap_dict = game_post_enrichment_overlap_instance.to_dict()
# create an instance of GamePostEnrichmentOverlap from a dict
game_post_enrichment_overlap_from_dict = GamePostEnrichmentOverlap.from_dict(game_post_enrichment_overlap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


