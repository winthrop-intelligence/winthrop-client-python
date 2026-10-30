# TournamentRoundCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TournamentRound]**](TournamentRound.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.tournament_round_collection import TournamentRoundCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TournamentRoundCollection from a JSON string
tournament_round_collection_instance = TournamentRoundCollection.from_json(json)
# print the JSON string representation of the object
print(TournamentRoundCollection.to_json())

# convert the object into a dict
tournament_round_collection_dict = tournament_round_collection_instance.to_dict()
# create an instance of TournamentRoundCollection from a dict
tournament_round_collection_from_dict = TournamentRoundCollection.from_dict(tournament_round_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


