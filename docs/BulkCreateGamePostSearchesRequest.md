# BulkCreateGamePostSearchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[BulkCreateGamePostSearchesRequestPostsInner]**](BulkCreateGamePostSearchesRequestPostsInner.md) |  | 
**season_start** | **date** | WINAD-10067: start of the edited season window. Intent and post reconciliation is scoped to this range so days in another season the grid never showed are never touched. | [optional] 
**season_end** | **date** | WINAD-10067: end of the edited season window. | [optional] 
**intents** | [**List[BulkCreateGamePostSearchesRequestIntentsInner]**](BulkCreateGamePostSearchesRequestIntentsInner.md) | WINAD-10067: the full staged open+pending grid state for the window. Open days carry their real deal-type ids; pending days carry the Pending GameType id. ScheduleIntents are reconciled to this set (upsert submitted days, delete window days no longer present). | [optional] 

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


