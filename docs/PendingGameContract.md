# PendingGameContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The RawContract id. | 
**school_id** | **int** |  | 
**school_name** | **str** |  | [optional] 
**foia_label_id** | **int** |  | [optional] 
**filename** | **str** |  | 
**drive_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**sha256** | **str** | SHA-256 of the PDF as uploaded. | 
**ocr_text_ready** | **bool** |  | 
**pending** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.pending_game_contract import PendingGameContract

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContract from a JSON string
pending_game_contract_instance = PendingGameContract.from_json(json)
# print the JSON string representation of the object
print(PendingGameContract.to_json())

# convert the object into a dict
pending_game_contract_dict = pending_game_contract_instance.to_dict()
# create an instance of PendingGameContract from a dict
pending_game_contract_from_dict = PendingGameContract.from_dict(pending_game_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


