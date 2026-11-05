# AdminSeasonStatsImportJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**arguments** | **List[object]** |  | [optional] 
**enqueued_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_season_stats_import_job import AdminSeasonStatsImportJob

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSeasonStatsImportJob from a JSON string
admin_season_stats_import_job_instance = AdminSeasonStatsImportJob.from_json(json)
# print the JSON string representation of the object
print(AdminSeasonStatsImportJob.to_json())

# convert the object into a dict
admin_season_stats_import_job_dict = admin_season_stats_import_job_instance.to_dict()
# create an instance of AdminSeasonStatsImportJob from a dict
admin_season_stats_import_job_from_dict = AdminSeasonStatsImportJob.from_dict(admin_season_stats_import_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


