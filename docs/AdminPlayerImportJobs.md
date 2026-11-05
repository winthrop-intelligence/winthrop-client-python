# AdminPlayerImportJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[AdminPlayerImportJobsJobsInner]**](AdminPlayerImportJobsJobsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_player_import_jobs import AdminPlayerImportJobs

# TODO update the JSON string below
json = "{}"
# create an instance of AdminPlayerImportJobs from a JSON string
admin_player_import_jobs_instance = AdminPlayerImportJobs.from_json(json)
# print the JSON string representation of the object
print(AdminPlayerImportJobs.to_json())

# convert the object into a dict
admin_player_import_jobs_dict = admin_player_import_jobs_instance.to_dict()
# create an instance of AdminPlayerImportJobs from a dict
admin_player_import_jobs_from_dict = AdminPlayerImportJobs.from_dict(admin_player_import_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


