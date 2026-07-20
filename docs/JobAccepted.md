# JobAccepted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**status** | **str** |  | 
**status_url** | **str** |  | 
**result_url** | **str** |  | 

## Example

```python
from winthrop_client_python.models.job_accepted import JobAccepted

# TODO update the JSON string below
json = "{}"
# create an instance of JobAccepted from a JSON string
job_accepted_instance = JobAccepted.from_json(json)
# print the JSON string representation of the object
print(JobAccepted.to_json())

# convert the object into a dict
job_accepted_dict = job_accepted_instance.to_dict()
# create an instance of JobAccepted from a dict
job_accepted_from_dict = JobAccepted.from_dict(job_accepted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


