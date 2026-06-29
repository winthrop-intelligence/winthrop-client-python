# GamePostSearchResultPostsInnerCreatedBy

Post creator. Present only with post_details=true.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**coach_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_posts_inner_created_by import GamePostSearchResultPostsInnerCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultPostsInnerCreatedBy from a JSON string
game_post_search_result_posts_inner_created_by_instance = GamePostSearchResultPostsInnerCreatedBy.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultPostsInnerCreatedBy.to_json())

# convert the object into a dict
game_post_search_result_posts_inner_created_by_dict = game_post_search_result_posts_inner_created_by_instance.to_dict()
# create an instance of GamePostSearchResultPostsInnerCreatedBy from a dict
game_post_search_result_posts_inner_created_by_from_dict = GamePostSearchResultPostsInnerCreatedBy.from_dict(game_post_search_result_posts_inner_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


