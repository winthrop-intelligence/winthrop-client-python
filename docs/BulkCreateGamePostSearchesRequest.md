# BulkCreateGamePostSearchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[BulkCreateGamePostSearchesRequestPostsInner]**](BulkCreateGamePostSearchesRequestPostsInner.md) |  | 

## Example

```python
from winthrop_client_python.models.bulk_create_game_post_searches_request import BulkCreateGamePostSearchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateGamePostSearchesRequest from a JSON string
bulk_create_game_post_searches_request_instance = BulkCreateGamePostSearchesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCreateGamePostSearchesRequest.to_json())

# convert the object into a dict
bulk_create_game_post_searches_request_dict = bulk_create_game_post_searches_request_instance.to_dict()
# create an instance of BulkCreateGamePostSearchesRequest from a dict
bulk_create_game_post_searches_request_from_dict = BulkCreateGamePostSearchesRequest.from_dict(bulk_create_game_post_searches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


