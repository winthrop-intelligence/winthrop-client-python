# PublishPendingGameContractRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_contract_id** | **int** |  | 
**expected_sha256** | **str** |  | 
**occurrences** | [**List[PublishPendingGameContractRequestOccurrencesInner]**](PublishPendingGameContractRequestOccurrencesInner.md) |  | 

## Example

```python
from winthrop_client_python.models.publish_pending_game_contract_request import PublishPendingGameContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishPendingGameContractRequest from a JSON string
publish_pending_game_contract_request_instance = PublishPendingGameContractRequest.from_json(json)
# print the JSON string representation of the object
print(PublishPendingGameContractRequest.to_json())

# convert the object into a dict
publish_pending_game_contract_request_dict = publish_pending_game_contract_request_instance.to_dict()
# create an instance of PublishPendingGameContractRequest from a dict
publish_pending_game_contract_request_from_dict = PublishPendingGameContractRequest.from_dict(publish_pending_game_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


