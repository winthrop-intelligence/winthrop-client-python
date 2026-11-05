# AdminPlayerImportJobsJobsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**arguments** | **List[object]** |  | [optional] 
**enqueued_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_import_jobs_jobs_inner import AdminPlayerImportJobsJobsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerImportJobsJobsInner from a JSON string
admin_player_import_jobs_jobs_inner_instance = AdminPlayerImportJobsJobsInner.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerImportJobsJobsInner.to_json())

# convert the object into a dict
admin_player_import_jobs_jobs_inner_dict = admin_player_import_jobs_jobs_inner_instance.to_dict()
# create an instance of AdminPlayerImportJobsJobsInner from a dict
admin_player_import_jobs_jobs_inner_from_dict = AdminPlayerImportJobsJobsInner.from_dict(admin_player_import_jobs_jobs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


