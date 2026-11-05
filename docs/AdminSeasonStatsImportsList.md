# AdminSeasonStatsImportsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminSeasonStatsImportsListMeta**](AdminSeasonStatsImportsListMeta.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_season_stats_imports_list import AdminSeasonStatsImportsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSeasonStatsImportsList from a JSON string
admin_season_stats_imports_list_instance = AdminSeasonStatsImportsList.from_json(json)
# print the JSON string representation of the object
print(AdminSeasonStatsImportsList.to_json())

# convert the object into a dict
admin_season_stats_imports_list_dict = admin_season_stats_imports_list_instance.to_dict()
# create an instance of AdminSeasonStatsImportsList from a dict
admin_season_stats_imports_list_from_dict = AdminSeasonStatsImportsList.from_dict(admin_season_stats_imports_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


