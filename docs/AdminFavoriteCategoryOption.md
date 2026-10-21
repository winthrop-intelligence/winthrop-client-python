# AdminFavoriteCategoryOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_favorite_category_option import AdminFavoriteCategoryOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFavoriteCategoryOption from a JSON string
admin_favorite_category_option_instance = AdminFavoriteCategoryOption.from_json(json)
# print the JSON string representation of the object
print(AdminFavoriteCategoryOption.to_json())

# convert the object into a dict
admin_favorite_category_option_dict = admin_favorite_category_option_instance.to_dict()
# create an instance of AdminFavoriteCategoryOption from a dict
admin_favorite_category_option_from_dict = AdminFavoriteCategoryOption.from_dict(admin_favorite_category_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


