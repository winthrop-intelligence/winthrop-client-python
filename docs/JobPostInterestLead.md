# JobPostInterestLead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**submitted_at** | **datetime** |  | [optional] 
**recruiter_email_enqueued_at** | **datetime** |  | [optional] 
**candidate** | [**JobPostInterestLeadCandidate**](JobPostInterestLeadCandidate.md) |  | [optional] 
**job** | [**JobPostInterestLeadJob**](JobPostInterestLeadJob.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_interest_lead import JobPostInterestLead

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostInterestLead from a JSON string
job_post_interest_lead_instance = JobPostInterestLead.from_json(json)
# print the JSON string representation of the object
print(JobPostInterestLead.to_json())

# convert the object into a dict
job_post_interest_lead_dict = job_post_interest_lead_instance.to_dict()
# create an instance of JobPostInterestLead from a dict
job_post_interest_lead_from_dict = JobPostInterestLead.from_dict(job_post_interest_lead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


