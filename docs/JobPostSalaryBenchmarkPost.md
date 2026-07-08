# JobPostSalaryBenchmarkPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**remote_id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**school** | **str** |  | [optional] 
**school_winad_id** | **int** |  | [optional] 
**posted_at** | **datetime** |  | [optional] 
**salary** | **str** |  | [optional] 
**posted_min_salary** | **float** |  | [optional] 
**posted_max_salary** | **float** |  | [optional] 
**pay_period** | **str** |  | [optional] 
**annualized_min** | **float** |  | [optional] 
**annualized_max** | **float** |  | [optional] 
**annualized_midpoint** | **float** |  | [optional] 
**normalization_note** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**departments** | **List[str]** |  | [optional] 
**sports** | **List[str]** |  | [optional] 
**outlier_side** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_salary_benchmark_post import JobPostSalaryBenchmarkPost

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostSalaryBenchmarkPost from a JSON string
job_post_salary_benchmark_post_instance = JobPostSalaryBenchmarkPost.from_json(json)
# print the JSON string representation of the object
print(JobPostSalaryBenchmarkPost.to_json())

# convert the object into a dict
job_post_salary_benchmark_post_dict = job_post_salary_benchmark_post_instance.to_dict()
# create an instance of JobPostSalaryBenchmarkPost from a dict
job_post_salary_benchmark_post_from_dict = JobPostSalaryBenchmarkPost.from_dict(job_post_salary_benchmark_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


