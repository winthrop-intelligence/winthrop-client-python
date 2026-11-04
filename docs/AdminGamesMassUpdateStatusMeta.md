# AdminGamesMassUpdateStatusMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[AdminGamesImportJob]**](AdminGamesImportJob.md) |  | [optional] 
**required_headers** | **List[str]** |  | [optional] 
**optional_headers** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_games_mass_update_status_meta import AdminGamesMassUpdateStatusMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGamesMassUpdateStatusMeta from a JSON string
admin_games_mass_update_status_meta_instance = AdminGamesMassUpdateStatusMeta.from_json(json)
# print the JSON string representation of the object
print(AdminGamesMassUpdateStatusMeta.to_json())

# convert the object into a dict
admin_games_mass_update_status_meta_dict = admin_games_mass_update_status_meta_instance.to_dict()
# create an instance of AdminGamesMassUpdateStatusMeta from a dict
admin_games_mass_update_status_meta_from_dict = AdminGamesMassUpdateStatusMeta.from_dict(admin_games_mass_update_status_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


