# AdminSeasonStatsImportsListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_headers** | **List[str]** |  | [optional] 
**optional_headers** | **List[str]** |  | [optional] 
**jobs** | [**List[AdminSeasonStatsImportJob]**](AdminSeasonStatsImportJob.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_season_stats_imports_list_meta import AdminSeasonStatsImportsListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSeasonStatsImportsListMeta from a JSON string
admin_season_stats_imports_list_meta_instance = AdminSeasonStatsImportsListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminSeasonStatsImportsListMeta.to_json())

# convert the object into a dict
admin_season_stats_imports_list_meta_dict = admin_season_stats_imports_list_meta_instance.to_dict()
# create an instance of AdminSeasonStatsImportsListMeta from a dict
admin_season_stats_imports_list_meta_from_dict = AdminSeasonStatsImportsListMeta.from_dict(admin_season_stats_imports_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


