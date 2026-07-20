# JobResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**ocr_run_id** | **str** |  | 
**status** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**policy_version** | **str** |  | [optional] 
**source_sha256** | **str** |  | [optional] 
**text** | **str** |  | 
**text_sha256** | **str** |  | 
**pages** | [**List[PageResult]**](PageResult.md) |  | 
**missing_pages** | **List[int]** |  | [optional] [default to []]
**summary** | **Dict[str, object]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_result import JobResult

# TODO update the JSON string below
json = "{}"
# create an instance of JobResult from a JSON string
job_result_instance = JobResult.from_json(json)
# print the JSON string representation of the object
print(JobResult.to_json())

# convert the object into a dict
job_result_dict = job_result_instance.to_dict()
# create an instance of JobResult from a dict
job_result_from_dict = JobResult.from_dict(job_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


