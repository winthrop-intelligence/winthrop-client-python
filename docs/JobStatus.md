# JobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**profile** | **str** |  | [optional] 
**page_count** | **int** |  | [optional] 
**progress** | [**JobProgress**](JobProgress.md) |  | 
**created_at** | **str** |  | [optional] 
**completed_at** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_status import JobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatus from a JSON string
job_status_instance = JobStatus.from_json(json)
# print the JSON string representation of the object
print(JobStatus.to_json())

# convert the object into a dict
job_status_dict = job_status_instance.to_dict()
# create an instance of JobStatus from a dict
job_status_from_dict = JobStatus.from_dict(job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


