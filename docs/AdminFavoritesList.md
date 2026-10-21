# AdminFavoritesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminFavorite]**](AdminFavorite.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_favorites_list import AdminFavoritesList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFavoritesList from a JSON string
admin_favorites_list_instance = AdminFavoritesList.from_json(json)
# print the JSON string representation of the object
print(AdminFavoritesList.to_json())

# convert the object into a dict
admin_favorites_list_dict = admin_favorites_list_instance.to_dict()
# create an instance of AdminFavoritesList from a dict
admin_favorites_list_from_dict = AdminFavoritesList.from_dict(admin_favorites_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


