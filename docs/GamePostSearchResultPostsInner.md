# GamePostSearchResultPostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | GamePost ID — the specific post this entry represents. | 
**var_date** | **date** |  | 
**game_types** | **List[str]** | Raw game-type names for this post (drive deal-type chip colors). | 
**status** | **str** | Present only with post_details&#x3D;true. | [optional] 
**start_date** | **date** | Present only with post_details&#x3D;true. | [optional] 
**end_date** | **date** | Present only with post_details&#x3D;true. | [optional] 
**description** | **str** | Present only with post_details&#x3D;true. | [optional] 
**game_types_display** | **str** | Comma-separated game type names. Present only with post_details&#x3D;true. | [optional] 
**expires_on** | **date** | Present only with post_details&#x3D;true. | [optional] 
**created_at** | **datetime** | Present only with post_details&#x3D;true. | [optional] 
**can_manage** | **bool** | Whether the current user can manage this post. Present only with post_details&#x3D;true. | [optional] 
**created_by** | [**GamePostSearchResultPostsInnerCreatedBy**](GamePostSearchResultPostsInnerCreatedBy.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_posts_inner import GamePostSearchResultPostsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultPostsInner from a JSON string
game_post_search_result_posts_inner_instance = GamePostSearchResultPostsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultPostsInner.to_json())

# convert the object into a dict
game_post_search_result_posts_inner_dict = game_post_search_result_posts_inner_instance.to_dict()
# create an instance of GamePostSearchResultPostsInner from a dict
game_post_search_result_posts_inner_from_dict = GamePostSearchResultPostsInner.from_dict(game_post_search_result_posts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


