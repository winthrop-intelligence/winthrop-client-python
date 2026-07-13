# GamePostSearchResultOverlapLineUpsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The specific date open on both sides (not the whole window). | 
**classification** | **str** | guarantee &#x3D; one side travels (GuaranteeNeeded) and the other hosts (GuaranteeOffered); home_and_home &#x3D; both marked HomeAndHome; any_format &#x3D; both sides willing to host and travel (agree on terms); mte &#x3D; both marked Tournament (multi-team event); neutral_site &#x3D; both marked Neutral; possible &#x3D; same date open but the deal types don&#39;t complement. | 
**strong** | **bool** | True for every actionable classification (guarantee, home_and_home, any_format, mte, neutral_site); false for possible. | 
**traveling_school_id** | **int** | School travelling (paid) on a guarantee line-up, or the viewer travelling to the poster&#39;s event on an \&quot;mte\&quot; line-up. Null on classifications that carry no direction. | [optional] 
**hosting_school_id** | **int** | School hosting (paying) on a guarantee line-up, or the poster hosting its event on an \&quot;mte\&quot; line-up. Null on classifications that carry no direction. | [optional] 
**traveling_school_name** | **str** | Resolved name of the traveling school for the row detail, present whenever the line-up carries a direction (guarantee or mte); null on classifications with no direction. | [optional] 
**hosting_school_name** | **str** | Resolved name of the hosting school for the row detail, present whenever the line-up carries a direction (guarantee or mte); null on classifications with no direction. | [optional] 
**possible_kind** | **str** | Why a possible line-up doesn&#39;t complement. Set only when classification is \&quot;possible\&quot;; null otherwise. | [optional] 
**flexible_side** | **str** | On a guarantee line-up, the side that was open to any format while the other pinned the direction (\&quot;viewer\&quot; &#x3D; the current user&#39;s school, \&quot;poster\&quot; &#x3D; the posting school). Drives the \&quot;· they&#39;re open to any format\&quot; / \&quot;· you&#39;re open on this date\&quot; clause. Null on a clean both-specific guarantee and on every other classification. | [optional] 
**viewer_wants** | **List[str]** | The viewer&#39;s marked deal types on a possible line-up (null on every other classification), so the card can name the mismatch — e.g. \&quot;you want a series\&quot;. | [optional] 
**poster_wants** | **List[str]** | The posting school&#39;s marked deal types on a possible line-up (null on every other classification), so the card can name the mismatch — e.g. \&quot;they want a paid road game\&quot;. | [optional] 

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


