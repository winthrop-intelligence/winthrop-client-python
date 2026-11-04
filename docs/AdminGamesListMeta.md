# AdminGamesListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**school** | [**AdminGameSchoolRef**](AdminGameSchoolRef.md) |  | [optional] 
**sports** | [**List[AdminGameSportRef]**](AdminGameSportRef.md) |  | [optional] 
**states** | [**List[AdminGameStateRef]**](AdminGameStateRef.md) |  | [optional] 
**season_years** | [**List[GetAdminPositionCopyOptions200ResponseSeasonsInner]**](GetAdminPositionCopyOptions200ResponseSeasonsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_games_list_meta import AdminGamesListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGamesListMeta from a JSON string
admin_games_list_meta_instance = AdminGamesListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminGamesListMeta.to_json())

# convert the object into a dict
admin_games_list_meta_dict = admin_games_list_meta_instance.to_dict()
# create an instance of AdminGamesListMeta from a dict
admin_games_list_meta_from_dict = AdminGamesListMeta.from_dict(admin_games_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


