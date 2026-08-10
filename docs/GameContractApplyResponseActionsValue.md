# GameContractApplyResponseActionsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game_contract_id** | **int** |  | 
**game_ids** | **List[int]** |  | 

## Example

```python
from winthrop_client_python.models.game_contract_apply_response_actions_value import GameContractApplyResponseActionsValue

# TODO update the JSON string below
json = "{}"
# create an instance of GameContractApplyResponseActionsValue from a JSON string
game_contract_apply_response_actions_value_instance = GameContractApplyResponseActionsValue.from_json(json)
# print the JSON string representation of the object
print(GameContractApplyResponseActionsValue.to_json())

# convert the object into a dict
game_contract_apply_response_actions_value_dict = game_contract_apply_response_actions_value_instance.to_dict()
# create an instance of GameContractApplyResponseActionsValue from a dict
game_contract_apply_response_actions_value_from_dict = GameContractApplyResponseActionsValue.from_dict(game_contract_apply_response_actions_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


