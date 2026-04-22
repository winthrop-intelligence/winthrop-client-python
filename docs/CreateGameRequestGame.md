# CreateGameRequestGame


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**home_school_id** | **int** |  | [optional] 
**away_school_id** | **int** |  | [optional] 
**sport_id** | **int** |  | [optional] 
**game_date** | **date** |  | [optional] 
**neutral** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_game_request_game import CreateGameRequestGame

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGameRequestGame from a JSON string
create_game_request_game_instance = CreateGameRequestGame.from_json(json)
# print the JSON string representation of the object
print(CreateGameRequestGame.to_json())

# convert the object into a dict
create_game_request_game_dict = create_game_request_game_instance.to_dict()
# create an instance of CreateGameRequestGame from a dict
create_game_request_game_from_dict = CreateGameRequestGame.from_dict(create_game_request_game_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


