# JobPostInterestLeadJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**posted_at** | **datetime** |  | [optional] 
**expired_at** | **datetime** |  | [optional] 
**school** | [**JobSchool**](JobSchool.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_interest_lead_job import JobPostInterestLeadJob

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostInterestLeadJob from a JSON string
job_post_interest_lead_job_instance = JobPostInterestLeadJob.from_json(json)
# print the JSON string representation of the object
print(JobPostInterestLeadJob.to_json())

# convert the object into a dict
job_post_interest_lead_job_dict = job_post_interest_lead_job_instance.to_dict()
# create an instance of JobPostInterestLeadJob from a dict
job_post_interest_lead_job_from_dict = JobPostInterestLeadJob.from_dict(job_post_interest_lead_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


