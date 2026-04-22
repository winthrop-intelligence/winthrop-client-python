# UpdateGamePostSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_post** | [**UpdateGamePostSearchRequestGamePost**](UpdateGamePostSearchRequestGamePost.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_game_post_search_request import UpdateGamePostSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGamePostSearchRequest from a JSON string
update_game_post_search_request_instance = UpdateGamePostSearchRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGamePostSearchRequest.to_json())

# convert the object into a dict
update_game_post_search_request_dict = update_game_post_search_request_instance.to_dict()
# create an instance of UpdateGamePostSearchRequest from a dict
update_game_post_search_request_from_dict = UpdateGamePostSearchRequest.from_dict(update_game_post_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


