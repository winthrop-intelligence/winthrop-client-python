# PendingGameContractReceipt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**schema_version** | **str** |  | 
**raw_contract_id** | **int** |  | 
**occurrences** | [**List[PendingGameContractReceiptOccurrencesInner]**](PendingGameContractReceiptOccurrencesInner.md) |  | 

## Example

```python
from winthrop_client_python.models.pending_game_contract_receipt import PendingGameContractReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractReceipt from a JSON string
pending_game_contract_receipt_instance = PendingGameContractReceipt.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractReceipt.to_json())

# convert the object into a dict
pending_game_contract_receipt_dict = pending_game_contract_receipt_instance.to_dict()
# create an instance of PendingGameContractReceipt from a dict
pending_game_contract_receipt_from_dict = PendingGameContractReceipt.from_dict(pending_game_contract_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


