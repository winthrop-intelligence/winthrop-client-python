# GameContractSeriesEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**comp_cents** | **int** |  | [optional] 
**comp_tbd** | **bool** |  | [optional] 
**variable** | **bool** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**cancelled** | **bool** |  | [optional] 
**season_year** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**game_date_tbd** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_contract_series_entry import GameContractSeriesEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GameContractSeriesEntry from a JSON string
game_contract_series_entry_instance = GameContractSeriesEntry.from_json(json)
# print the JSON string representation of the object
print(GameContractSeriesEntry.to_json())

# convert the object into a dict
game_contract_series_entry_dict = game_contract_series_entry_instance.to_dict()
# create an instance of GameContractSeriesEntry from a dict
game_contract_series_entry_from_dict = GameContractSeriesEntry.from_dict(game_contract_series_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


