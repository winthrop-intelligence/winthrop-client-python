# PendingGameContractReceiptOccurrencesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occurrence_id** | **str** |  | 
**disposition** | **str** |  | 
**game_ids** | **List[int]** | Only for a write. | [optional] 
**game_contract_id** | **int** | Only for a write. | [optional] 
**reason** | **str** | Only for a skip, the approved reason. | [optional] 

## Example

```python
from winthrop_client_python.models.pending_game_contract_receipt_occurrences_inner import PendingGameContractReceiptOccurrencesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractReceiptOccurrencesInner from a JSON string
pending_game_contract_receipt_occurrences_inner_instance = PendingGameContractReceiptOccurrencesInner.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractReceiptOccurrencesInner.to_json())

# convert the object into a dict
pending_game_contract_receipt_occurrences_inner_dict = pending_game_contract_receipt_occurrences_inner_instance.to_dict()
# create an instance of PendingGameContractReceiptOccurrencesInner from a dict
pending_game_contract_receipt_occurrences_inner_from_dict = PendingGameContractReceiptOccurrencesInner.from_dict(pending_game_contract_receipt_occurrences_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


