# JobPostCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JobPost]**](JobPost.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.job_post_collection import JobPostCollection

# TODO update the JSON string below
json = "{}"
# create an instance of JobPostCollection from a JSON string
job_post_collection_instance = JobPostCollection.from_json(json)
# print the JSON string representation of the object
print JobPostCollection.to_json()

# convert the object into a dict
job_post_collection_dict = job_post_collection_instance.to_dict()
# create an instance of JobPostCollection from a dict
job_post_collection_form_dict = job_post_collection.from_dict(job_post_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


