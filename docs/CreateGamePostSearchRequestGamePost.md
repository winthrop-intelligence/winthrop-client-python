# CreateGamePostSearchRequestGamePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**start_date** | **date** |  | 
**end_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**game_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_game_post_search_request_game_post import CreateGamePostSearchRequestGamePost

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGamePostSearchRequestGamePost from a JSON string
create_game_post_search_request_game_post_instance = CreateGamePostSearchRequestGamePost.from_json(json)
# print the JSON string representation of the object
print(CreateGamePostSearchRequestGamePost.to_json())

# convert the object into a dict
create_game_post_search_request_game_post_dict = create_game_post_search_request_game_post_instance.to_dict()
# create an instance of CreateGamePostSearchRequestGamePost from a dict
create_game_post_search_request_game_post_from_dict = CreateGamePostSearchRequestGamePost.from_dict(create_game_post_search_request_game_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


