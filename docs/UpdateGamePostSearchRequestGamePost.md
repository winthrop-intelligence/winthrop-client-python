# UpdateGamePostSearchRequestGamePost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**expires_on** | **date** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**game_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_game_post_search_request_game_post import UpdateGamePostSearchRequestGamePost

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGamePostSearchRequestGamePost from a JSON string
update_game_post_search_request_game_post_instance = UpdateGamePostSearchRequestGamePost.from_json(json)
# print the JSON string representation of the object
print(UpdateGamePostSearchRequestGamePost.to_json())

# convert the object into a dict
update_game_post_search_request_game_post_dict = update_game_post_search_request_game_post_instance.to_dict()
# create an instance of UpdateGamePostSearchRequestGamePost from a dict
update_game_post_search_request_game_post_from_dict = UpdateGamePostSearchRequestGamePost.from_dict(update_game_post_search_request_game_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


