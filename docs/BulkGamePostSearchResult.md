# BulkGamePostSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_game_post_search_result import BulkGamePostSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGamePostSearchResult from a JSON string
bulk_game_post_search_result_instance = BulkGamePostSearchResult.from_json(json)
# print the JSON string representation of the object
print(BulkGamePostSearchResult.to_json())

# convert the object into a dict
bulk_game_post_search_result_dict = bulk_game_post_search_result_instance.to_dict()
# create an instance of BulkGamePostSearchResult from a dict
bulk_game_post_search_result_from_dict = BulkGamePostSearchResult.from_dict(bulk_game_post_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


