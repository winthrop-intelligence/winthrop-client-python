# GamePostSearchResultOverlapLineUpsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The specific date open on both sides (not the whole window). | 
**classification** | **str** | guarantee &#x3D; one side travels (GuaranteeNeeded) and the other hosts (GuaranteeOffered); home_and_home &#x3D; both marked HomeAndHome; possible &#x3D; same date open but the deal types don&#39;t complement. | 
**strong** | **bool** | True for guarantee and home-and-home; false for possible. | 
**traveling_school_id** | **int** | School travelling (paid) on a guarantee line-up. Set only when classification is \&quot;guarantee\&quot;; null otherwise. | [optional] 
**hosting_school_id** | **int** | School hosting (paying) on a guarantee line-up. Set only when classification is \&quot;guarantee\&quot;; null otherwise. | [optional] 
**traveling_school_name** | **str** | Resolved name of the traveling school for the guarantee-row detail; null on non-guarantee line-ups. | [optional] 
**hosting_school_name** | **str** | Resolved name of the hosting school for the guarantee-row detail; null on non-guarantee line-ups. | [optional] 
**possible_kind** | **str** | Why a possible line-up doesn&#39;t complement. Set only when classification is \&quot;possible\&quot;; null otherwise. | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_overlap_line_ups_inner import GamePostSearchResultOverlapLineUpsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultOverlapLineUpsInner from a JSON string
game_post_search_result_overlap_line_ups_inner_instance = GamePostSearchResultOverlapLineUpsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultOverlapLineUpsInner.to_json())

# convert the object into a dict
game_post_search_result_overlap_line_ups_inner_dict = game_post_search_result_overlap_line_ups_inner_instance.to_dict()
# create an instance of GamePostSearchResultOverlapLineUpsInner from a dict
game_post_search_result_overlap_line_ups_inner_from_dict = GamePostSearchResultOverlapLineUpsInner.from_dict(game_post_search_result_overlap_line_ups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


