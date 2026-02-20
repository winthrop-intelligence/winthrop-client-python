# GamePostSearchResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GamePostSearchResult]**](GamePostSearchResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_post_search_result_collection import GamePostSearchResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GamePostSearchResultCollection from a JSON string
game_post_search_result_collection_instance = GamePostSearchResultCollection.from_json(json)
# print the JSON string representation of the object
print(GamePostSearchResultCollection.to_json())

# convert the object into a dict
game_post_search_result_collection_dict = game_post_search_result_collection_instance.to_dict()
# create an instance of GamePostSearchResultCollection from a dict
game_post_search_result_collection_from_dict = GamePostSearchResultCollection.from_dict(game_post_search_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


