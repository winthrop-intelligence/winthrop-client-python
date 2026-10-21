# AdminUsersListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**filter_options** | [**AdminUsersListMetaFilterOptions**](AdminUsersListMetaFilterOptions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_users_list_meta import AdminUsersListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUsersListMeta from a JSON string
admin_users_list_meta_instance = AdminUsersListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminUsersListMeta.to_json())

# convert the object into a dict
admin_users_list_meta_dict = admin_users_list_meta_instance.to_dict()
# create an instance of AdminUsersListMeta from a dict
admin_users_list_meta_from_dict = AdminUsersListMeta.from_dict(admin_users_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


