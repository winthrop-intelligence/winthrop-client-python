# AdminRequestedItemListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**filter_options** | [**AdminRequestedItemListMetaAllOfFilterOptions**](AdminRequestedItemListMetaAllOfFilterOptions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_requested_item_list_meta import AdminRequestedItemListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRequestedItemListMeta from a JSON string
admin_requested_item_list_meta_instance = AdminRequestedItemListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminRequestedItemListMeta.to_json())

# convert the object into a dict
admin_requested_item_list_meta_dict = admin_requested_item_list_meta_instance.to_dict()
# create an instance of AdminRequestedItemListMeta from a dict
admin_requested_item_list_meta_from_dict = AdminRequestedItemListMeta.from_dict(admin_requested_item_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


