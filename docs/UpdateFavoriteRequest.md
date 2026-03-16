# UpdateFavoriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorites_category_id** | **int** | The category ID to assign the favorite to | [optional] 

## Example

```python
from winthrop_client_python.models.update_favorite_request import UpdateFavoriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFavoriteRequest from a JSON string
update_favorite_request_instance = UpdateFavoriteRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFavoriteRequest.to_json())

# convert the object into a dict
update_favorite_request_dict = update_favorite_request_instance.to_dict()
# create an instance of UpdateFavoriteRequest from a dict
update_favorite_request_from_dict = UpdateFavoriteRequest.from_dict(update_favorite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


