# AdminSeasonStatsEditorListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**school** | [**IdName**](IdName.md) |  | [optional] 
**year** | **int** |  | [optional] 
**schools** | [**List[IdName]**](IdName.md) |  | [optional] 
**years** | **List[int]** |  | [optional] 
**fields** | [**List[AdminSeasonStatsEditorField]**](AdminSeasonStatsEditorField.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_season_stats_editor_list_meta import AdminSeasonStatsEditorListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSeasonStatsEditorListMeta from a JSON string
admin_season_stats_editor_list_meta_instance = AdminSeasonStatsEditorListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminSeasonStatsEditorListMeta.to_json())

# convert the object into a dict
admin_season_stats_editor_list_meta_dict = admin_season_stats_editor_list_meta_instance.to_dict()
# create an instance of AdminSeasonStatsEditorListMeta from a dict
admin_season_stats_editor_list_meta_from_dict = AdminSeasonStatsEditorListMeta.from_dict(admin_season_stats_editor_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


