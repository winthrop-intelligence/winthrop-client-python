# JobPostSalaryBenchmark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolved_scope** | [**JobPostSalaryBenchmarkScope**](JobPostSalaryBenchmarkScope.md) |  | [optional] 
**sample** | [**JobPostSalaryBenchmarkSample**](JobPostSalaryBenchmarkSample.md) |  | [optional] 
**posted_salary_summary** | [**JobPostSalarySummary**](JobPostSalarySummary.md) |  | [optional] 
**salary_basis_notes** | [**JobPostSalaryBenchmarkSalaryBasisNotes**](JobPostSalaryBenchmarkSalaryBasisNotes.md) |  | [optional] 
**representative_posts** | [**List[JobPostSalaryBenchmarkPost]**](JobPostSalaryBenchmarkPost.md) |  | [optional] 
**outliers** | [**List[JobPostSalaryBenchmarkPost]**](JobPostSalaryBenchmarkPost.md) |  | [optional] 
**coverage_notes** | **List[str]** |  | [optional] 
**provenance** | [**JobPostSalaryBenchmarkProvenance**](JobPostSalaryBenchmarkProvenance.md) |  | [optional] 
**why_empty** | **str** |  | [optional] 
**relaxation_suggestions** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_salary_benchmark import JobPostSalaryBenchmark

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostSalaryBenchmark from a JSON string
job_post_salary_benchmark_instance = JobPostSalaryBenchmark.from_json(json)
# print the JSON string representation of the object
print(JobPostSalaryBenchmark.to_json())

# convert the object into a dict
job_post_salary_benchmark_dict = job_post_salary_benchmark_instance.to_dict()
# create an instance of JobPostSalaryBenchmark from a dict
job_post_salary_benchmark_from_dict = JobPostSalaryBenchmark.from_dict(job_post_salary_benchmark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


