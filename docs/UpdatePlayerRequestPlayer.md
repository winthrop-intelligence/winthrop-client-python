# UpdatePlayerRequestPlayer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**external_code** | **str** |  | [optional] 
**height** | **int** |  | [optional] 
**weight** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_player_request_player import UpdatePlayerRequestPlayer

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlayerRequestPlayer from a JSON string
update_player_request_player_instance = UpdatePlayerRequestPlayer.from_json(json)
# print the JSON string representation of the object
print(UpdatePlayerRequestPlayer.to_json())

# convert the object into a dict
update_player_request_player_dict = update_player_request_player_instance.to_dict()
# create an instance of UpdatePlayerRequestPlayer from a dict
update_player_request_player_from_dict = UpdatePlayerRequestPlayer.from_dict(update_player_request_player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


