# CreateJobJson

JSON body for pull-based sources (Google Drive).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**JobSource**](JobSource.md) |  | 
**profile** | **str** |  | [optional] [default to 'default']
**options** | [**JobOptions**](JobOptions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_job_json import CreateJobJson

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJobJson from a JSON string
create_job_json_instance = CreateJobJson.from_json(json)
# print the JSON string representation of the object
print(CreateJobJson.to_json())

# convert the object into a dict
create_job_json_dict = create_job_json_instance.to_dict()
# create an instance of CreateJobJson from a dict
create_job_json_from_dict = CreateJobJson.from_dict(create_job_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


