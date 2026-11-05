# CreatePlayerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**CreatePlayerRequestPlayer**](CreatePlayerRequestPlayer.md) |  | 

## Example

```python
from winthrop_client_python.models.create_player_request import CreatePlayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlayerRequest from a JSON string
create_player_request_instance = CreatePlayerRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePlayerRequest.to_json())

# convert the object into a dict
create_player_request_dict = create_player_request_instance.to_dict()
# create an instance of CreatePlayerRequest from a dict
create_player_request_from_dict = CreatePlayerRequest.from_dict(create_player_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


