# JobPostInterestLeadCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**claimed_coach_id** | **str** |  | [optional] 
**claimed_profile_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_interest_lead_candidate import JobPostInterestLeadCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostInterestLeadCandidate from a JSON string
job_post_interest_lead_candidate_instance = JobPostInterestLeadCandidate.from_json(json)
# print the JSON string representation of the object
print(JobPostInterestLeadCandidate.to_json())

# convert the object into a dict
job_post_interest_lead_candidate_dict = job_post_interest_lead_candidate_instance.to_dict()
# create an instance of JobPostInterestLeadCandidate from a dict
job_post_interest_lead_candidate_from_dict = JobPostInterestLeadCandidate.from_dict(job_post_interest_lead_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


