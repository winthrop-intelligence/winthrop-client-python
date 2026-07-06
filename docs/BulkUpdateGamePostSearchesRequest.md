# BulkUpdateGamePostSearchesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_group_id** | **UUID** | The publish group (card) being edited. | 
**description** | **str** | New shared message applied to every post that stays on the card. | [optional] 
**posts** | [**List[BulkUpdateGamePostSearchesRequestPostsInner]**](BulkUpdateGamePostSearchesRequestPostsInner.md) |  | 
**season_start** | **date** | WINAD-10067: start of the edited season window. Intent reconciliation is scoped to this range. | [optional] 
**season_end** | **date** | WINAD-10067: end of the edited season window. | [optional] 
**intents** | [**List[BulkCreateGamePostSearchesRequestIntentsInner]**](BulkCreateGamePostSearchesRequestIntentsInner.md) | WINAD-10067: the full staged open+pending grid state for the window. Open days carry their real deal-type ids; pending days carry the Pending GameType id. ScheduleIntents are reconciled to this set (days another card still owns are preserved). | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_update_game_post_searches_request import BulkUpdateGamePostSearchesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateGamePostSearchesRequest from a JSON string
bulk_update_game_post_searches_request_instance = BulkUpdateGamePostSearchesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateGamePostSearchesRequest.to_json())

# convert the object into a dict
bulk_update_game_post_searches_request_dict = bulk_update_game_post_searches_request_instance.to_dict()
# create an instance of BulkUpdateGamePostSearchesRequest from a dict
bulk_update_game_post_searches_request_from_dict = BulkUpdateGamePostSearchesRequest.from_dict(bulk_update_game_post_searches_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


