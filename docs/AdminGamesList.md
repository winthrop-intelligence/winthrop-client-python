# AdminGamesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminGamesListMeta**](AdminGamesListMeta.md) |  | [optional] 
**data** | [**List[AdminGame]**](AdminGame.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_games_list import AdminGamesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGamesList from a JSON string
admin_games_list_instance = AdminGamesList.from_json(json)
# print the JSON string representation of the object
print(AdminGamesList.to_json())

# convert the object into a dict
admin_games_list_dict = admin_games_list_instance.to_dict()
# create an instance of AdminGamesList from a dict
admin_games_list_from_dict = AdminGamesList.from_dict(admin_games_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


