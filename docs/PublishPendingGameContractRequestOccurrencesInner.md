# PublishPendingGameContractRequestOccurrencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurrence_id** | **str** |  | 
**game_ids** | **List[int]** |  | 
**expected_games** | [**List[PendingGameContractWriteExpectedGamesInner]**](PendingGameContractWriteExpectedGamesInner.md) |  | 
**game_contract** | [**PendingGameContractWriteGameContract**](PendingGameContractWriteGameContract.md) |  | 
**skip** | [**PendingGameContractSkipSkip**](PendingGameContractSkipSkip.md) |  | 

## Example

```python
from winthrop_client_python.models.publish_pending_game_contract_request_occurrences_inner import PublishPendingGameContractRequestOccurrencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPendingGameContractRequestOccurrencesInner from a JSON string
publish_pending_game_contract_request_occurrences_inner_instance = PublishPendingGameContractRequestOccurrencesInner.from_json(json)
# print the JSON string representation of the object
print(PublishPendingGameContractRequestOccurrencesInner.to_json())

# convert the object into a dict
publish_pending_game_contract_request_occurrences_inner_dict = publish_pending_game_contract_request_occurrences_inner_instance.to_dict()
# create an instance of PublishPendingGameContractRequestOccurrencesInner from a dict
publish_pending_game_contract_request_occurrences_inner_from_dict = PublishPendingGameContractRequestOccurrencesInner.from_dict(publish_pending_game_contract_request_occurrences_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


