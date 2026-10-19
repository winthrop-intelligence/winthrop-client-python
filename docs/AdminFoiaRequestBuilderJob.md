# AdminFoiaRequestBuilderJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**job_type** | **str** |  | [optional] 
**user_email** | **str** |  | [optional] 
**arguments** | **List[object]** |  | [optional] 
**enqueued_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_request_builder_job import AdminFoiaRequestBuilderJob

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaRequestBuilderJob from a JSON string
admin_foia_request_builder_job_instance = AdminFoiaRequestBuilderJob.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaRequestBuilderJob.to_json())

# convert the object into a dict
admin_foia_request_builder_job_dict = admin_foia_request_builder_job_instance.to_dict()
# create an instance of AdminFoiaRequestBuilderJob from a dict
admin_foia_request_builder_job_from_dict = AdminFoiaRequestBuilderJob.from_dict(admin_foia_request_builder_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


