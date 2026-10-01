# GamePostEnrichmentPostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**season_year** | **int** |  | [optional] 
**outside_target_season** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_enrichment_posts_inner import GamePostEnrichmentPostsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostEnrichmentPostsInner from a JSON string
game_post_enrichment_posts_inner_instance = GamePostEnrichmentPostsInner.from_json(json)
# print the JSON string representation of the object
print(GamePostEnrichmentPostsInner.to_json())

# convert the object into a dict
game_post_enrichment_posts_inner_dict = game_post_enrichment_posts_inner_instance.to_dict()
# create an instance of GamePostEnrichmentPostsInner from a dict
game_post_enrichment_posts_inner_from_dict = GamePostEnrichmentPostsInner.from_dict(game_post_enrichment_posts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


