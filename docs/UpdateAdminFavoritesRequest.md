# UpdateAdminFavoritesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite** | [**UpdateAdminFavoritesRequestFavorite**](UpdateAdminFavoritesRequestFavorite.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_favorites_request import UpdateAdminFavoritesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminFavoritesRequest from a JSON string
update_admin_favorites_request_instance = UpdateAdminFavoritesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminFavoritesRequest.to_json())

# convert the object into a dict
update_admin_favorites_request_dict = update_admin_favorites_request_instance.to_dict()
# create an instance of UpdateAdminFavoritesRequest from a dict
update_admin_favorites_request_from_dict = UpdateAdminFavoritesRequest.from_dict(update_admin_favorites_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


