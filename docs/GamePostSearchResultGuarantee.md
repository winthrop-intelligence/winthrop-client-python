# GamePostSearchResultGuarantee

WINAD-10054: the school's 3-yr median guarantee economics (from SchoolGuaranteeEconomicsBatchQuery) — what it typically receives when it travels and pays when it hosts, in cents. Medians/estimates, labelled \"3-yr median\" in the UI (rounded, e.g. $90K), never a hard quote. Each side is null when the school has no qualifying history; the whole block is null when it has neither, or when the viewer lacks the guarantee- aggregate grant — the UI hides the chip rather than showing $0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_median_cents** | **int** | 3-yr median guarantee paid as the home/host team; null when no history. | [optional] 
**host_sample_size** | **int** | Number of host money-games behind the median. | [optional] 
**travel_median_cents** | **int** | 3-yr median guarantee received as the away/traveling team; null when no history. | [optional] 
**travel_sample_size** | **int** | Number of travel money-games behind the median. | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_guarantee import GamePostSearchResultGuarantee

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultGuarantee from a JSON string
game_post_search_result_guarantee_instance = GamePostSearchResultGuarantee.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultGuarantee.to_json())

# convert the object into a dict
game_post_search_result_guarantee_dict = game_post_search_result_guarantee_instance.to_dict()
# create an instance of GamePostSearchResultGuarantee from a dict
game_post_search_result_guarantee_from_dict = GamePostSearchResultGuarantee.from_dict(game_post_search_result_guarantee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


