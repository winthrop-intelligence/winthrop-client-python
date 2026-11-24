# PendingGameContractSkip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurrence_id** | **str** |  | 
**skip** | [**PendingGameContractSkipSkip**](PendingGameContractSkipSkip.md) |  | 

## Example

```python
from winthrop_client_python.models.pending_game_contract_skip import PendingGameContractSkip

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractSkip from a JSON string
pending_game_contract_skip_instance = PendingGameContractSkip.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractSkip.to_json())

# convert the object into a dict
pending_game_contract_skip_dict = pending_game_contract_skip_instance.to_dict()
# create an instance of PendingGameContractSkip from a dict
pending_game_contract_skip_from_dict = PendingGameContractSkip.from_dict(pending_game_contract_skip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


