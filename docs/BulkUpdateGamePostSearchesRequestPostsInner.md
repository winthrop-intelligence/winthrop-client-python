# BulkUpdateGamePostSearchesRequestPostsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**var_date** | **date** | The post&#39;s single open day (end_date stays null). Required — the server keys each card post by its day and rejects an item with no date. | 
**game_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_update_game_post_searches_request_posts_inner import BulkUpdateGamePostSearchesRequestPostsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateGamePostSearchesRequestPostsInner from a JSON string
bulk_update_game_post_searches_request_posts_inner_instance = BulkUpdateGamePostSearchesRequestPostsInner.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateGamePostSearchesRequestPostsInner.to_json())

# convert the object into a dict
bulk_update_game_post_searches_request_posts_inner_dict = bulk_update_game_post_searches_request_posts_inner_instance.to_dict()
# create an instance of BulkUpdateGamePostSearchesRequestPostsInner from a dict
bulk_update_game_post_searches_request_posts_inner_from_dict = BulkUpdateGamePostSearchesRequestPostsInner.from_dict(bulk_update_game_post_searches_request_posts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


