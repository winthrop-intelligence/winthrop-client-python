# AdminUsersListMetaFilterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_types** | [**List[IdName]**](IdName.md) |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_users_list_meta_filter_options import AdminUsersListMetaFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUsersListMetaFilterOptions from a JSON string
admin_users_list_meta_filter_options_instance = AdminUsersListMetaFilterOptions.from_json(json)
# print the JSON string representation of the object
print(AdminUsersListMetaFilterOptions.to_json())

# convert the object into a dict
admin_users_list_meta_filter_options_dict = admin_users_list_meta_filter_options_instance.to_dict()
# create an instance of AdminUsersListMetaFilterOptions from a dict
admin_users_list_meta_filter_options_from_dict = AdminUsersListMetaFilterOptions.from_dict(admin_users_list_meta_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


