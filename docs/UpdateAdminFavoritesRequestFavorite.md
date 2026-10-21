# UpdateAdminFavoritesRequestFavorite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorites_category_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_favorites_request_favorite import UpdateAdminFavoritesRequestFavorite

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFavoritesRequestFavorite from a JSON string
update_admin_favorites_request_favorite_instance = UpdateAdminFavoritesRequestFavorite.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFavoritesRequestFavorite.to_json())

# convert the object into a dict
update_admin_favorites_request_favorite_dict = update_admin_favorites_request_favorite_instance.to_dict()
# create an instance of UpdateAdminFavoritesRequestFavorite from a dict
update_admin_favorites_request_favorite_from_dict = UpdateAdminFavoritesRequestFavorite.from_dict(update_admin_favorites_request_favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


