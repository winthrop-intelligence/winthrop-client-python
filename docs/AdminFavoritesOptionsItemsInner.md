# AdminFavoritesOptionsItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_favorites_options_items_inner import AdminFavoritesOptionsItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFavoritesOptionsItemsInner from a JSON string
admin_favorites_options_items_inner_instance = AdminFavoritesOptionsItemsInner.from_json(json)
# print the JSON string representation of the object
print(AdminFavoritesOptionsItemsInner.to_json())

# convert the object into a dict
admin_favorites_options_items_inner_dict = admin_favorites_options_items_inner_instance.to_dict()
# create an instance of AdminFavoritesOptionsItemsInner from a dict
admin_favorites_options_items_inner_from_dict = AdminFavoritesOptionsItemsInner.from_dict(admin_favorites_options_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


