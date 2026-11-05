# CreatePlayerStatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_stat** | [**CreatePlayerStatRequestPlayerStat**](CreatePlayerStatRequestPlayerStat.md) |  | 

## Example

```python
from winthrop_client_python.models.create_player_stat_request import CreatePlayerStatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlayerStatRequest from a JSON string
create_player_stat_request_instance = CreatePlayerStatRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePlayerStatRequest.to_json())

# convert the object into a dict
create_player_stat_request_dict = create_player_stat_request_instance.to_dict()
# create an instance of CreatePlayerStatRequest from a dict
create_player_stat_request_from_dict = CreatePlayerStatRequest.from_dict(create_player_stat_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


