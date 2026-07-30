# JobPostDisagreementCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | [**List[JobPostDisagreement]**](JobPostDisagreement.md) |  | [optional] 
**new_truncated** | **bool** | True if new_page is not the last page for the \&quot;new\&quot; section. | [optional] 
**new_total_count** | **int** | Total number of \&quot;new\&quot; rows across all pages. | [optional] 
**still_pending** | [**List[JobPostDisagreement]**](JobPostDisagreement.md) |  | [optional] 
**still_pending_truncated** | **bool** | True if still_pending_page is not the last page for the \&quot;still_pending\&quot; section. | [optional] 
**still_pending_total_count** | **int** | Total number of \&quot;still_pending\&quot; rows across all pages. | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_disagreement_collection import JobPostDisagreementCollection

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostDisagreementCollection from a JSON string
job_post_disagreement_collection_instance = JobPostDisagreementCollection.from_json(json)
# print the JSON string representation of the object
print(JobPostDisagreementCollection.to_json())

# convert the object into a dict
job_post_disagreement_collection_dict = job_post_disagreement_collection_instance.to_dict()
# create an instance of JobPostDisagreementCollection from a dict
job_post_disagreement_collection_from_dict = JobPostDisagreementCollection.from_dict(job_post_disagreement_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


