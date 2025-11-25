# JobCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Job]**](Job.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_collection import JobCollection

# TODO update the JSON string below
json = "{}"
# create an instance of JobCollection from a JSON string
job_collection_instance = JobCollection.from_json(json)
# print the JSON string representation of the object
print(JobCollection.to_json())

# convert the object into a dict
job_collection_dict = job_collection_instance.to_dict()
# create an instance of JobCollection from a dict
job_collection_from_dict = JobCollection.from_dict(job_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


