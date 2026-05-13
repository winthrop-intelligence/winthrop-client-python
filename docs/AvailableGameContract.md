# AvailableGameContract

Row returned by /games/available_contracts — a lightweight projection of GameContract for picking from the Edit Game sheet's Contract dropdown. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**sport_name** | **str** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_tbd** | **str** |  | [optional] 
**game_type** | **str** | One of Guarantee, Neutral, Tournament, Exhibition. | [optional] 
**comp_cents** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.available_game_contract import AvailableGameContract

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableGameContract from a JSON string
available_game_contract_instance = AvailableGameContract.from_json(json)
# print the JSON string representation of the object
print(AvailableGameContract.to_json())

# convert the object into a dict
available_game_contract_dict = available_game_contract_instance.to_dict()
# create an instance of AvailableGameContract from a dict
available_game_contract_from_dict = AvailableGameContract.from_dict(available_game_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


