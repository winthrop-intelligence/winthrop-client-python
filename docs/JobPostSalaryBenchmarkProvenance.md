# JobPostSalaryBenchmarkProvenance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of** | **datetime** |  | [optional] 
**source** | **str** |  | [optional] 
**source_basis** | **str** |  | [optional] 
**source_updated_at** | **datetime** |  | [optional] 
**confidence** | **str** |  | [optional] 
**permission_filtered_count** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_salary_benchmark_provenance import JobPostSalaryBenchmarkProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostSalaryBenchmarkProvenance from a JSON string
job_post_salary_benchmark_provenance_instance = JobPostSalaryBenchmarkProvenance.from_json(json)
# print the JSON string representation of the object
print(JobPostSalaryBenchmarkProvenance.to_json())

# convert the object into a dict
job_post_salary_benchmark_provenance_dict = job_post_salary_benchmark_provenance_instance.to_dict()
# create an instance of JobPostSalaryBenchmarkProvenance from a dict
job_post_salary_benchmark_provenance_from_dict = JobPostSalaryBenchmarkProvenance.from_dict(job_post_salary_benchmark_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


