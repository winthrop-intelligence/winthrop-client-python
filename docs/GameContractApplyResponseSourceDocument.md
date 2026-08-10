# GameContractApplyResponseSourceDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**byte_size** | **int** |  | 
**sha256** | **str** |  | 

## Example

```python
from winthrop_client_python.models.game_contract_apply_response_source_document import GameContractApplyResponseSourceDocument

# TODO update the JSON string below
json = "{}"
# create an instance of GameContractApplyResponseSourceDocument from a JSON string
game_contract_apply_response_source_document_instance = GameContractApplyResponseSourceDocument.from_json(json)
# print the JSON string representation of the object
print(GameContractApplyResponseSourceDocument.to_json())

# convert the object into a dict
game_contract_apply_response_source_document_dict = game_contract_apply_response_source_document_instance.to_dict()
# create an instance of GameContractApplyResponseSourceDocument from a dict
game_contract_apply_response_source_document_from_dict = GameContractApplyResponseSourceDocument.from_dict(game_contract_apply_response_source_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


