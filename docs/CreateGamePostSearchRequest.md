# CreateGamePostSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_post** | [**CreateGamePostSearchRequestGamePost**](CreateGamePostSearchRequestGamePost.md) |  | 

## Example

```python
from winthrop_client_python.models.create_game_post_search_request import CreateGamePostSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGamePostSearchRequest from a JSON string
create_game_post_search_request_instance = CreateGamePostSearchRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGamePostSearchRequest.to_json())

# convert the object into a dict
create_game_post_search_request_dict = create_game_post_search_request_instance.to_dict()
# create an instance of CreateGamePostSearchRequest from a dict
create_game_post_search_request_from_dict = CreateGamePostSearchRequest.from_dict(create_game_post_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


