# GameContractSeriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**home_school_id** | **int** |  | [optional] 
**home_school_name** | **str** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**away_school_name** | **str** |  | [optional] 
**game_type** | **str** |  | [optional] 
**season_year** | **int** |  | [optional] 
**cancel_fee_cents** | **int** |  | [optional] 
**has_raw_contract** | **bool** |  | [optional] 
**raw_contract_url** | **str** |  | [optional] 
**data** | [**List[GameContractSeriesEntry]**](GameContractSeriesEntry.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.game_contract_series_response import GameContractSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GameContractSeriesResponse from a JSON string
game_contract_series_response_instance = GameContractSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(GameContractSeriesResponse.to_json())

# convert the object into a dict
game_contract_series_response_dict = game_contract_series_response_instance.to_dict()
# create an instance of GameContractSeriesResponse from a dict
game_contract_series_response_from_dict = GameContractSeriesResponse.from_dict(game_contract_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


