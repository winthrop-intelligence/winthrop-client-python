# TournamentRound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**round** | **int** |  | [optional] 
**tournament_id** | **int** |  | [optional] 
**tournament_name** | **str** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**sport_name** | **str** |  | [optional] 
**sport_name_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.tournament_round import TournamentRound

# TODO update the JSON string below
json = "{}"
# create an instance of TournamentRound from a JSON string
tournament_round_instance = TournamentRound.from_json(json)
# print the JSON string representation of the object
print(TournamentRound.to_json())

# convert the object into a dict
tournament_round_dict = tournament_round_instance.to_dict()
# create an instance of TournamentRound from a dict
tournament_round_from_dict = TournamentRound.from_dict(tournament_round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


