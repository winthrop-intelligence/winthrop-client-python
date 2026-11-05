# AdminSeasonStatsEditorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminSeasonStatsEditorListMeta**](AdminSeasonStatsEditorListMeta.md) |  | [optional] 
**data** | [**List[AdminSeasonStatsEditorSeason]**](AdminSeasonStatsEditorSeason.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_season_stats_editor_list import AdminSeasonStatsEditorList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSeasonStatsEditorList from a JSON string
admin_season_stats_editor_list_instance = AdminSeasonStatsEditorList.from_json(json)
# print the JSON string representation of the object
print(AdminSeasonStatsEditorList.to_json())

# convert the object into a dict
admin_season_stats_editor_list_dict = admin_season_stats_editor_list_instance.to_dict()
# create an instance of AdminSeasonStatsEditorList from a dict
admin_season_stats_editor_list_from_dict = AdminSeasonStatsEditorList.from_dict(admin_season_stats_editor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


