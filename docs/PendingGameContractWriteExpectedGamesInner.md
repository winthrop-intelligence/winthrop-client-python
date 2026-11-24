# PendingGameContractWriteExpectedGamesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**home_school_id** | **int** |  | 
**away_school_id** | **int** |  | 
**sport_id** | **int** |  | 
**game_date** | **date** |  | 
**season_year** | **int** |  | 
**season_year_tbd** | **int** |  | 
**neutral** | **bool** | The Game&#39;s neutral-site flag, rechecked in the transaction. | 
**game_contract_id** | **int** | Must be null. | 

## Example

```python
from winthrop_client_python.models.pending_game_contract_write_expected_games_inner import PendingGameContractWriteExpectedGamesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PendingGameContractWriteExpectedGamesInner from a JSON string
pending_game_contract_write_expected_games_inner_instance = PendingGameContractWriteExpectedGamesInner.from_json(json)
# print the JSON string representation of the object
print(PendingGameContractWriteExpectedGamesInner.to_json())

# convert the object into a dict
pending_game_contract_write_expected_games_inner_dict = pending_game_contract_write_expected_games_inner_instance.to_dict()
# create an instance of PendingGameContractWriteExpectedGamesInner from a dict
pending_game_contract_write_expected_games_inner_from_dict = PendingGameContractWriteExpectedGamesInner.from_dict(pending_game_contract_write_expected_games_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


