# AdminSchoolUploadJob

One in-progress/enqueued update_school_info_importer Sidekiq job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | [optional] 
**arguments** | **List[object]** |  | [optional] 
**enqueued_at** | **datetime** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_upload_job import AdminSchoolUploadJob

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolUploadJob from a JSON string
admin_school_upload_job_instance = AdminSchoolUploadJob.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolUploadJob.to_json())

# convert the object into a dict
admin_school_upload_job_dict = admin_school_upload_job_instance.to_dict()
# create an instance of AdminSchoolUploadJob from a dict
admin_school_upload_job_from_dict = AdminSchoolUploadJob.from_dict(admin_school_upload_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


