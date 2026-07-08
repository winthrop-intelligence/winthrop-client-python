# JobPostSalarySummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**basis** | **str** |  | [optional] 
**summary_basis** | **str** | Indicates whether summary statistics use raw posted values or annualized comparison values. | [optional] 
**min** | **float** |  | [optional] 
**p25** | **float** |  | [optional] 
**median** | **float** |  | [optional] 
**p75** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**average_midpoint** | **float** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_salary_summary import JobPostSalarySummary

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostSalarySummary from a JSON string
job_post_salary_summary_instance = JobPostSalarySummary.from_json(json)
# print the JSON string representation of the object
print(JobPostSalarySummary.to_json())

# convert the object into a dict
job_post_salary_summary_dict = job_post_salary_summary_instance.to_dict()
# create an instance of JobPostSalarySummary from a dict
job_post_salary_summary_from_dict = JobPostSalarySummary.from_dict(job_post_salary_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


