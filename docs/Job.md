# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**job_url** | **str** |  | [optional] 
**posted_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**school** | [**JobSchool**](JobSchool.md) |  | [optional] 
**departments** | [**List[JobDepartment]**](JobDepartment.md) |  | [optional] 
**sports** | [**List[JobSport]**](JobSport.md) |  | [optional] 
**candidates** | [**List[JobCandidate]**](JobCandidate.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_form_dict = job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


