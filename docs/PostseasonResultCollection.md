# PostseasonResultCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PostseasonResult]**](PostseasonResult.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.postseason_result_collection import PostseasonResultCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PostseasonResultCollection from a JSON string
postseason_result_collection_instance = PostseasonResultCollection.from_json(json)
# print the JSON string representation of the object
print(PostseasonResultCollection.to_json())

# convert the object into a dict
postseason_result_collection_dict = postseason_result_collection_instance.to_dict()
# create an instance of PostseasonResultCollection from a dict
postseason_result_collection_from_dict = PostseasonResultCollection.from_dict(postseason_result_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


