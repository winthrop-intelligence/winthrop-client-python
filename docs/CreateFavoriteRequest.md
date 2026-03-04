# CreateFavoriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favoritable_type** | **str** | The model type (e.g. \&quot;Coach\&quot;) | 
**favoritable_id** | **int** | The ID of the record to favorite | 

## Example

```python
from winthrop_client_python.models.create_favorite_request import CreateFavoriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFavoriteRequest from a JSON string
create_favorite_request_instance = CreateFavoriteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFavoriteRequest.to_json())

# convert the object into a dict
create_favorite_request_dict = create_favorite_request_instance.to_dict()
# create an instance of CreateFavoriteRequest from a dict
create_favorite_request_from_dict = CreateFavoriteRequest.from_dict(create_favorite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


