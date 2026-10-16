# AdminRequestedItemListMetaAllOfFilterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**List[AdminRequestedItemFilterOption]**](AdminRequestedItemFilterOption.md) |  | [optional] 
**schools** | [**List[AdminRequestedItemFilterOption]**](AdminRequestedItemFilterOption.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_requested_item_list_meta_all_of_filter_options import AdminRequestedItemListMetaAllOfFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRequestedItemListMetaAllOfFilterOptions from a JSON string
admin_requested_item_list_meta_all_of_filter_options_instance = AdminRequestedItemListMetaAllOfFilterOptions.from_json(json)
# print the JSON string representation of the object
print(AdminRequestedItemListMetaAllOfFilterOptions.to_json())

# convert the object into a dict
admin_requested_item_list_meta_all_of_filter_options_dict = admin_requested_item_list_meta_all_of_filter_options_instance.to_dict()
# create an instance of AdminRequestedItemListMetaAllOfFilterOptions from a dict
admin_requested_item_list_meta_all_of_filter_options_from_dict = AdminRequestedItemListMetaAllOfFilterOptions.from_dict(admin_requested_item_list_meta_all_of_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


