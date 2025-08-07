# JobPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**uid** | **str** |  | 
**work_type** | **str** |  | [optional] 
**description** | **str** |  | 
**description_md** | **str** |  | [optional] 
**salary_summary** | **str** |  | [optional] 
**annual_salary** | **float** |  | [optional] 
**pay_period** | **str** |  | [optional] 
**min_salary** | **float** |  | [optional] 
**max_salary** | **float** |  | [optional] 
**school_id** | **int** |  | 
**required_years_of_experience** | **int** |  | [optional] 
**expired** | **bool** |  | [optional] [default to False]
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**categories** | [**List[Category]**](Category.md) |  | [optional] 
**ml_is_athletics** | **bool** |  | [optional] 
**llm_is_athletics** | **bool** |  | [optional] 
**human_override_is_athletics** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post import JobPost

# TODO update the JSON string below
json = "{}"
# create an instance of JobPost from a JSON string
job_post_instance = JobPost.from_json(json)
# print the JSON string representation of the object
print(JobPost.to_json())

# convert the object into a dict
job_post_dict = job_post_instance.to_dict()
# create an instance of JobPost from a dict
job_post_form_dict = job_post.from_dict(job_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


