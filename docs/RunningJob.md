# RunningJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**active** | **int** |  | [optional] 
**succeeded** | **int** |  | [optional] 
**failed** | **int** |  | [optional] 
**start_time** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.running_job import RunningJob

# TODO update the JSON string below
json = "{}"
# create an instance of RunningJob from a JSON string
running_job_instance = RunningJob.from_json(json)
# print the JSON string representation of the object
print(RunningJob.to_json())

# convert the object into a dict
running_job_dict = running_job_instance.to_dict()
# create an instance of RunningJob from a dict
running_job_from_dict = RunningJob.from_dict(running_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


