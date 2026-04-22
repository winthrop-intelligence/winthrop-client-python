# CreateGameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game** | [**CreateGameRequestGame**](CreateGameRequestGame.md) |  | 

## Example

```python
from winthrop_client_python.models.create_game_request import CreateGameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGameRequest from a JSON string
create_game_request_instance = CreateGameRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGameRequest.to_json())

# convert the object into a dict
create_game_request_dict = create_game_request_instance.to_dict()
# create an instance of CreateGameRequest from a dict
create_game_request_from_dict = CreateGameRequest.from_dict(create_game_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


