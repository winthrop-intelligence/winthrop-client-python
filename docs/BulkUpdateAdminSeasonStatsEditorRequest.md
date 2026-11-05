# BulkUpdateAdminSeasonStatsEditorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seasons** | **Dict[str, Dict[str, str]]** | Season id &#x3D;&gt; any subset of the editable season stat fields as strings; an empty string clears the value | 

## Example

```python
from winthrop_client_python.models.bulk_update_admin_season_stats_editor_request import BulkUpdateAdminSeasonStatsEditorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateAdminSeasonStatsEditorRequest from a JSON string
bulk_update_admin_season_stats_editor_request_instance = BulkUpdateAdminSeasonStatsEditorRequest.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateAdminSeasonStatsEditorRequest.to_json())

# convert the object into a dict
bulk_update_admin_season_stats_editor_request_dict = bulk_update_admin_season_stats_editor_request_instance.to_dict()
# create an instance of BulkUpdateAdminSeasonStatsEditorRequest from a dict
bulk_update_admin_season_stats_editor_request_from_dict = BulkUpdateAdminSeasonStatsEditorRequest.from_dict(bulk_update_admin_season_stats_editor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


