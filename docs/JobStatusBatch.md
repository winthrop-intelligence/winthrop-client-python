# JobStatusBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[JobStatus]**](JobStatus.md) |  | 
**not_found** | **List[str]** |  | [optional] [default to []]

## Example

```python
from winthrop_client_python.models.job_status_batch import JobStatusBatch

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusBatch from a JSON string
job_status_batch_instance = JobStatusBatch.from_json(json)
# print the JSON string representation of the object
print(JobStatusBatch.to_json())

# convert the object into a dict
job_status_batch_dict = job_status_batch_instance.to_dict()
# create an instance of JobStatusBatch from a dict
job_status_batch_from_dict = JobStatusBatch.from_dict(job_status_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


