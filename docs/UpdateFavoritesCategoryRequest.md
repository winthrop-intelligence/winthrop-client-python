# UpdateFavoritesCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new category name | 

## Example

```python
from winthrop_client_python.models.update_favorites_category_request import UpdateFavoritesCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFavoritesCategoryRequest from a JSON string
update_favorites_category_request_instance = UpdateFavoritesCategoryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFavoritesCategoryRequest.to_json())

# convert the object into a dict
update_favorites_category_request_dict = update_favorites_category_request_instance.to_dict()
# create an instance of UpdateFavoritesCategoryRequest from a dict
update_favorites_category_request_from_dict = UpdateFavoritesCategoryRequest.from_dict(update_favorites_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


