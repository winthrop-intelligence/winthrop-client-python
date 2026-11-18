# PendingGameContractWriteGameContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_school_id** | **int** | May be null only for a Tournament. | 
**away_school_id** | **int** |  | 
**sport_id** | **int** |  | 
**game_type** | **str** |  | 
**game_date** | **date** |  | 
**game_date_tbd** | **str** |  | 
**comp_cents** | **int** |  | 
**comp_tbd** | **bool** |  | 
**variable** | **bool** |  | 
**cancel_fee_cents** | **int** |  | 
**signed_on** | **date** |  | 
**off_site_location** | **str** |  | 
**verified** | **bool** | Optional; published rows are never verified. | [optional] 

## Example

```python
from winthrop_client_python.models.pending_game_contract_write_game_contract import PendingGameContractWriteGameContract

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractWriteGameContract from a JSON string
pending_game_contract_write_game_contract_instance = PendingGameContractWriteGameContract.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractWriteGameContract.to_json())

# convert the object into a dict
pending_game_contract_write_game_contract_dict = pending_game_contract_write_game_contract_instance.to_dict()
# create an instance of PendingGameContractWriteGameContract from a dict
pending_game_contract_write_game_contract_from_dict = PendingGameContractWriteGameContract.from_dict(pending_game_contract_write_game_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


