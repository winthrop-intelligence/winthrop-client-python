# UpdateAdminFoiaRequestGamesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foia_request** | [**UpdateAdminFoiaRequestGamesRequestFoiaRequest**](UpdateAdminFoiaRequestGamesRequestFoiaRequest.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_foia_request_games_request import UpdateAdminFoiaRequestGamesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFoiaRequestGamesRequest from a JSON string
update_admin_foia_request_games_request_instance = UpdateAdminFoiaRequestGamesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFoiaRequestGamesRequest.to_json())

# convert the object into a dict
update_admin_foia_request_games_request_dict = update_admin_foia_request_games_request_instance.to_dict()
# create an instance of UpdateAdminFoiaRequestGamesRequest from a dict
update_admin_foia_request_games_request_from_dict = UpdateAdminFoiaRequestGamesRequest.from_dict(update_admin_foia_request_games_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


