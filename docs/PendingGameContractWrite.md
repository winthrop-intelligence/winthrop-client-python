# PendingGameContractWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurrence_id** | **str** |  | 
**game_ids** | **List[int]** |  | 
**expected_games** | [**List[PendingGameContractWriteExpectedGamesInner]**](PendingGameContractWriteExpectedGamesInner.md) |  | 
**game_contract** | [**PendingGameContractWriteGameContract**](PendingGameContractWriteGameContract.md) |  | 

## Example

```python
from winthrop_client_python.models.pending_game_contract_write import PendingGameContractWrite

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractWrite from a JSON string
pending_game_contract_write_instance = PendingGameContractWrite.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractWrite.to_json())

# convert the object into a dict
pending_game_contract_write_dict = pending_game_contract_write_instance.to_dict()
# create an instance of PendingGameContractWrite from a dict
pending_game_contract_write_from_dict = PendingGameContractWrite.from_dict(pending_game_contract_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


