# BulkCreateGamesRequestGamesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_school_id** | **int** |  | 
**away_school_id** | **int** |  | 
**sport_id** | **int** |  | 
**game_date** | **date** |  | [optional] 
**neutral** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.bulk_create_games_request_games_inner import BulkCreateGamesRequestGamesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCreateGamesRequestGamesInner from a JSON string
bulk_create_games_request_games_inner_instance = BulkCreateGamesRequestGamesInner.from_json(json)
# print the JSON string representation of the object
print(BulkCreateGamesRequestGamesInner.to_json())

# convert the object into a dict
bulk_create_games_request_games_inner_dict = bulk_create_games_request_games_inner_instance.to_dict()
# create an instance of BulkCreateGamesRequestGamesInner from a dict
bulk_create_games_request_games_inner_from_dict = BulkCreateGamesRequestGamesInner.from_dict(bulk_create_games_request_games_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


