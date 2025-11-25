# JobCandidate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**favorite_id** | **int** |  | [optional] 
**created_by_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**shortlisted** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_candidate import JobCandidate

# TODO update the JSON string below
json = "{}"
# create an instance of JobCandidate from a JSON string
job_candidate_instance = JobCandidate.from_json(json)
# print the JSON string representation of the object
print(JobCandidate.to_json())

# convert the object into a dict
job_candidate_dict = job_candidate_instance.to_dict()
# create an instance of JobCandidate from a dict
job_candidate_from_dict = JobCandidate.from_dict(job_candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


