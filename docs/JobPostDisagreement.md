# JobPostDisagreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_post_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**school_name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**llm_is_athletics** | **bool** |  | [optional] 
**ml_is_athletics** | **bool** |  | [optional] 
**reasoning** | **str** |  | [optional] 
**admin_url** | **str** |  | [optional] 
**novelty** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_disagreement import JobPostDisagreement

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostDisagreement from a JSON string
job_post_disagreement_instance = JobPostDisagreement.from_json(json)
# print the JSON string representation of the object
print(JobPostDisagreement.to_json())

# convert the object into a dict
job_post_disagreement_dict = job_post_disagreement_instance.to_dict()
# create an instance of JobPostDisagreement from a dict
job_post_disagreement_from_dict = JobPostDisagreement.from_dict(job_post_disagreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


