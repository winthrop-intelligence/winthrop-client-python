# GamePostSearchResultPostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**game_types** | **List[str]** | Raw game-type names for this posted day (drive deal-type chip colors). | 

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


