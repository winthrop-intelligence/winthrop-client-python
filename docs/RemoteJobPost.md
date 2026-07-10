# RemoteJobPost

Full Central Jobs job post snapshot. Required nullable fields must be sent with null when blank.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Remote job post ID | 
**uid** | **str** |  | [optional] 
**title** | **str** |  | 
**link** | **str** |  | 
**work_type** | **str** |  | 
**description_md** | **str** |  | 
**salary_summary** | **str** |  | 
**school_id** | **int** | Remote school WinAD ID | 
**expired** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**annual_salary** | **float** |  | 
**min_salary** | **float** |  | 
**max_salary** | **float** |  | 
**pay_period** | **str** |  | 
**required_years_of_experience** | **int** |  | 

## Example

```python
from winthrop_client_python.models.remote_job_post import RemoteJobPost

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteJobPost from a JSON string
remote_job_post_instance = RemoteJobPost.from_json(json)
# print the JSON string representation of the object
print(RemoteJobPost.to_json())

# convert the object into a dict
remote_job_post_dict = remote_job_post_instance.to_dict()
# create an instance of RemoteJobPost from a dict
remote_job_post_from_dict = RemoteJobPost.from_dict(remote_job_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


