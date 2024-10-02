# JobSchool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**winad_id** | **int** | ID of School, You can view Alma Mater using School API | [optional] 

## Example

```python
from winthrop_client_python.models.job_school import JobSchool

# TODO update the JSON string below
json = "{}"
# create an instance of JobSchool from a JSON string
job_school_instance = JobSchool.from_json(json)
# print the JSON string representation of the object
print(JobSchool.to_json())

# convert the object into a dict
job_school_dict = job_school_instance.to_dict()
# create an instance of JobSchool from a dict
job_school_form_dict = job_school.from_dict(job_school_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


