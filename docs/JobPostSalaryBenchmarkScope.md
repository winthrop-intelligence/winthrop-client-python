# JobPostSalaryBenchmarkScope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_query** | **str** |  | [optional] 
**role_terms** | **List[str]** |  | [optional] 
**department** | **str** |  | [optional] 
**sport** | **str** |  | [optional] 
**conference** | **str** |  | [optional] 
**division** | **str** |  | [optional] 
**school_query** | **str** |  | [optional] 
**peer_set** | **List[str]** |  | [optional] 
**date_window** | [**JobPostSalaryBenchmarkScopeDateWindow**](JobPostSalaryBenchmarkScopeDateWindow.md) |  | [optional] 
**salary_basis** | **str** |  | [optional] 
**response_format** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_salary_benchmark_scope import JobPostSalaryBenchmarkScope

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostSalaryBenchmarkScope from a JSON string
job_post_salary_benchmark_scope_instance = JobPostSalaryBenchmarkScope.from_json(json)
# print the JSON string representation of the object
print(JobPostSalaryBenchmarkScope.to_json())

# convert the object into a dict
job_post_salary_benchmark_scope_dict = job_post_salary_benchmark_scope_instance.to_dict()
# create an instance of JobPostSalaryBenchmarkScope from a dict
job_post_salary_benchmark_scope_from_dict = JobPostSalaryBenchmarkScope.from_dict(job_post_salary_benchmark_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


