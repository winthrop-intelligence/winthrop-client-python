# AdminFavoritesOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**favoritable_types** | **List[str]** |  | [optional] 
**items** | [**List[AdminFavoritesOptionsItemsInner]**](AdminFavoritesOptionsItemsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_favorites_options import AdminFavoritesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFavoritesOptions from a JSON string
admin_favorites_options_instance = AdminFavoritesOptions.from_json(json)
# print the JSON string representation of the object
print(AdminFavoritesOptions.to_json())

# convert the object into a dict
admin_favorites_options_dict = admin_favorites_options_instance.to_dict()
# create an instance of AdminFavoritesOptions from a dict
admin_favorites_options_from_dict = AdminFavoritesOptions.from_dict(admin_favorites_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


