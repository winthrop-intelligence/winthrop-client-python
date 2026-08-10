# GameContractApplyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** |  | 
**status** | **str** |  | 
**review_series_id** | **str** |  | 
**review_revision_sha256** | **str** |  | 
**decision_sha256** | **str** |  | 
**request_sha256** | **str** |  | 
**actor** | [**GameContractApplyResponseActor**](GameContractApplyResponseActor.md) |  | 
**raw_contract_id** | **int** |  | 
**actions** | [**Dict[str, GameContractApplyResponseActionsValue]**](GameContractApplyResponseActionsValue.md) | Map of approved action_id to the created GameContract and its linked Game ids | 
**source_document** | [**GameContractApplyResponseSourceDocument**](GameContractApplyResponseSourceDocument.md) |  | 
**pdf_processing** | [**GameContractApplyResponsePdfProcessing**](GameContractApplyResponsePdfProcessing.md) |  | 

## Example

```python
from winthrop_client_python.models.game_contract_apply_response import GameContractApplyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GameContractApplyResponse from a JSON string
game_contract_apply_response_instance = GameContractApplyResponse.from_json(json)
# print the JSON string representation of the object
print(GameContractApplyResponse.to_json())

# convert the object into a dict
game_contract_apply_response_dict = game_contract_apply_response_instance.to_dict()
# create an instance of GameContractApplyResponse from a dict
game_contract_apply_response_from_dict = GameContractApplyResponse.from_dict(game_contract_apply_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


