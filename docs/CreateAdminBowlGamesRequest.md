# CreateAdminBowlGamesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bowl_game** | [**CreateAdminBowlGamesRequestBowlGame**](CreateAdminBowlGamesRequestBowlGame.md) |  | 

## Example

```python
from winthrop_client_python.models.create_admin_bowl_games_request import CreateAdminBowlGamesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminBowlGamesRequest from a JSON string
create_admin_bowl_games_request_instance = CreateAdminBowlGamesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminBowlGamesRequest.to_json())

# convert the object into a dict
create_admin_bowl_games_request_dict = create_admin_bowl_games_request_instance.to_dict()
# create an instance of CreateAdminBowlGamesRequest from a dict
create_admin_bowl_games_request_from_dict = CreateAdminBowlGamesRequest.from_dict(create_admin_bowl_games_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


