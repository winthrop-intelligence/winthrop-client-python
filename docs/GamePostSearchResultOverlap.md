# GamePostSearchResultOverlap

WINAD-10052/10053: availability overlap between the requesting viewer's own school and this posting school for the sport, computed by AvailabilityOverlapMatcher. Both sides are read from schedule_intents, so every lined-up date is a subset of the availability the card shows. Always present; when the viewer has no school (e.g. a super-admin or conference account) or no dates line up, total is 0 with an empty line_ups array (the no-overlap state, never an error).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Number of dates that line up on both sides. | 
**strong_count** | **int** | How many lined-up dates are strong (any actionable classification: guarantee, home_and_home, any_format, mte, or neutral_site). | 
**rollup_text** | **str** | Ready-made pill summary, e.g. \&quot;3 dates line up · 2 strong\&quot;. Null when there is no overlap (total 0). | [optional] 
**line_ups** | [**List[GamePostSearchResultOverlapLineUpsInner]**](GamePostSearchResultOverlapLineUpsInner.md) | One entry per lined-up date, strong first (guarantee, home-and-home, any_format, mte, neutral_site), then possible; ties ordered by date. | 

## Example

```python
from winthrop_client_python.models.game_post_search_result_overlap import GamePostSearchResultOverlap

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultOverlap from a JSON string
game_post_search_result_overlap_instance = GamePostSearchResultOverlap.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultOverlap.to_json())

# convert the object into a dict
game_post_search_result_overlap_dict = game_post_search_result_overlap_instance.to_dict()
# create an instance of GamePostSearchResultOverlap from a dict
game_post_search_result_overlap_from_dict = GamePostSearchResultOverlap.from_dict(game_post_search_result_overlap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


