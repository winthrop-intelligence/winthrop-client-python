# CreateFavoritesCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The category name | 

## Example

```python
from winthrop_client_python.models.create_favorites_category_request import CreateFavoritesCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFavoritesCategoryRequest from a JSON string
create_favorites_category_request_instance = CreateFavoritesCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFavoritesCategoryRequest.to_json())

# convert the object into a dict
create_favorites_category_request_dict = create_favorites_category_request_instance.to_dict()
# create an instance of CreateFavoritesCategoryRequest from a dict
create_favorites_category_request_from_dict = CreateFavoritesCategoryRequest.from_dict(create_favorites_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


