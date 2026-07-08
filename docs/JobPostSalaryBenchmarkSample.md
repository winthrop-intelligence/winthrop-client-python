# JobPostSalaryBenchmarkSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_matching_posts** | **int** |  | [optional] 
**posts_with_structured_salary** | **int** |  | [optional] 
**posts_with_salary_text_only** | **int** |  | [optional] 
**posts_without_salary** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_salary_benchmark_sample import JobPostSalaryBenchmarkSample

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostSalaryBenchmarkSample from a JSON string
job_post_salary_benchmark_sample_instance = JobPostSalaryBenchmarkSample.from_json(json)
# print the JSON string representation of the object
print(JobPostSalaryBenchmarkSample.to_json())

# convert the object into a dict
job_post_salary_benchmark_sample_dict = job_post_salary_benchmark_sample_instance.to_dict()
# create an instance of JobPostSalaryBenchmarkSample from a dict
job_post_salary_benchmark_sample_from_dict = JobPostSalaryBenchmarkSample.from_dict(job_post_salary_benchmark_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


