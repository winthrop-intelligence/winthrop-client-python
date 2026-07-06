# BulkCreateGamePostSearchesRequestIntentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sport_id** | **int** |  | 
**var_date** | **date** |  | [optional] 
**game_type_ids** | **List[int]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_create_game_post_searches_request_intents_inner import BulkCreateGamePostSearchesRequestIntentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateGamePostSearchesRequestIntentsInner from a JSON string
bulk_create_game_post_searches_request_intents_inner_instance = BulkCreateGamePostSearchesRequestIntentsInner.from_json(json)
# print the JSON string representation of the object
print(BulkCreateGamePostSearchesRequestIntentsInner.to_json())

# convert the object into a dict
bulk_create_game_post_searches_request_intents_inner_dict = bulk_create_game_post_searches_request_intents_inner_instance.to_dict()
# create an instance of BulkCreateGamePostSearchesRequestIntentsInner from a dict
bulk_create_game_post_searches_request_intents_inner_from_dict = BulkCreateGamePostSearchesRequestIntentsInner.from_dict(bulk_create_game_post_searches_request_intents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


