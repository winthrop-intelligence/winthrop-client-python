# JobPost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**uid** | **str** |  | 
**work_type** | **str** |  | [optional] 
**description** | **str** |  | 
**school_id** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post import JobPost

# TODO update the JSON string below
json = "{}"
# create an instance of JobPost from a JSON string
job_post_instance = JobPost.from_json(json)
# print the JSON string representation of the object
print JobPost.to_json()

# convert the object into a dict
job_post_dict = job_post_instance.to_dict()
# create an instance of JobPost from a dict
job_post_form_dict = job_post.from_dict(job_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


