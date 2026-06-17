# BulkCreateGamePostSearchesRequestPostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**start_date** | **date** |  | 
**description** | **str** |  | [optional] 
**game_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_create_game_post_searches_request_posts_inner import BulkCreateGamePostSearchesRequestPostsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateGamePostSearchesRequestPostsInner from a JSON string
bulk_create_game_post_searches_request_posts_inner_instance = BulkCreateGamePostSearchesRequestPostsInner.from_json(json)
# print the JSON string representation of the object
print(BulkCreateGamePostSearchesRequestPostsInner.to_json())

# convert the object into a dict
bulk_create_game_post_searches_request_posts_inner_dict = bulk_create_game_post_searches_request_posts_inner_instance.to_dict()
# create an instance of BulkCreateGamePostSearchesRequestPostsInner from a dict
bulk_create_game_post_searches_request_posts_inner_from_dict = BulkCreateGamePostSearchesRequestPostsInner.from_dict(bulk_create_game_post_searches_request_posts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


