# AdminNotesListMetaFilterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[IdName]**](IdName.md) |  | [optional] 
**notable_types** | **List[str]** |  | [optional] 
**notable_items** | [**List[AdminNotesListMetaFilterOptionsNotableItemsInner]**](AdminNotesListMetaFilterOptionsNotableItemsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_notes_list_meta_filter_options import AdminNotesListMetaFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNotesListMetaFilterOptions from a JSON string
admin_notes_list_meta_filter_options_instance = AdminNotesListMetaFilterOptions.from_json(json)
# print the JSON string representation of the object
print(AdminNotesListMetaFilterOptions.to_json())

# convert the object into a dict
admin_notes_list_meta_filter_options_dict = admin_notes_list_meta_filter_options_instance.to_dict()
# create an instance of AdminNotesListMetaFilterOptions from a dict
admin_notes_list_meta_filter_options_from_dict = AdminNotesListMetaFilterOptions.from_dict(admin_notes_list_meta_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


