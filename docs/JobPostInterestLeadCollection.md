# JobPostInterestLeadCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobPostInterestLead]**](JobPostInterestLead.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_interest_lead_collection import JobPostInterestLeadCollection

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostInterestLeadCollection from a JSON string
job_post_interest_lead_collection_instance = JobPostInterestLeadCollection.from_json(json)
# print the JSON string representation of the object
print(JobPostInterestLeadCollection.to_json())

# convert the object into a dict
job_post_interest_lead_collection_dict = job_post_interest_lead_collection_instance.to_dict()
# create an instance of JobPostInterestLeadCollection from a dict
job_post_interest_lead_collection_from_dict = JobPostInterestLeadCollection.from_dict(job_post_interest_lead_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


