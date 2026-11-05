# UpdatePlayerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player** | [**UpdatePlayerRequestPlayer**](UpdatePlayerRequestPlayer.md) |  | 

## Example

```python
from winthrop_client_python.models.update_player_request import UpdatePlayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePlayerRequest from a JSON string
update_player_request_instance = UpdatePlayerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePlayerRequest.to_json())

# convert the object into a dict
update_player_request_dict = update_player_request_instance.to_dict()
# create an instance of UpdatePlayerRequest from a dict
update_player_request_from_dict = UpdatePlayerRequest.from_dict(update_player_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


