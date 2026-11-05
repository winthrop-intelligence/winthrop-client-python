# CreatePlayerRequestPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**external_code** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**weight** | **int** |  | [optional] 
**player_stats_attributes** | [**List[CreatePlayerRequestPlayerPlayerStatsAttributesInner]**](CreatePlayerRequestPlayerPlayerStatsAttributesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_player_request_player import CreatePlayerRequestPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlayerRequestPlayer from a JSON string
create_player_request_player_instance = CreatePlayerRequestPlayer.from_json(json)
# print the JSON string representation of the object
print(CreatePlayerRequestPlayer.to_json())

# convert the object into a dict
create_player_request_player_dict = create_player_request_player_instance.to_dict()
# create an instance of CreatePlayerRequestPlayer from a dict
create_player_request_player_from_dict = CreatePlayerRequestPlayer.from_dict(create_player_request_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


