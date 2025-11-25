# GameContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**game_date** | **datetime** |  | [optional] 
**game_date_tbd** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**variable** | **bool** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**signed_on** | **datetime** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**comp_tbd** | **bool** |  | [optional] 
**tbd** | **bool** |  | [optional] 
**season_year_tbd** | **int** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**season_year** | **int** |  | [optional] 
**game_type** | **str** |  | [optional] 
**off_site_location** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_contract import GameContract

# TODO update the JSON string below
json = "{}"
# create an instance of GameContract from a JSON string
game_contract_instance = GameContract.from_json(json)
# print the JSON string representation of the object
print(GameContract.to_json())

# convert the object into a dict
game_contract_dict = game_contract_instance.to_dict()
# create an instance of GameContract from a dict
game_contract_from_dict = GameContract.from_dict(game_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


