# GameDetailAllOfGameContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**game_type** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**signed_on** | **date** |  | [optional] 
**off_site_location** | **str** |  | [optional] 
**file_url** | **str** | Only present when a raw contract file is attached | [optional] 
**has_file** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_detail_all_of_game_contract import GameDetailAllOfGameContract

# TODO update the JSON string below
json = "{}"
# create an instance of GameDetailAllOfGameContract from a JSON string
game_detail_all_of_game_contract_instance = GameDetailAllOfGameContract.from_json(json)
# print the JSON string representation of the object
print(GameDetailAllOfGameContract.to_json())

# convert the object into a dict
game_detail_all_of_game_contract_dict = game_detail_all_of_game_contract_instance.to_dict()
# create an instance of GameDetailAllOfGameContract from a dict
game_detail_all_of_game_contract_from_dict = GameDetailAllOfGameContract.from_dict(game_detail_all_of_game_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


