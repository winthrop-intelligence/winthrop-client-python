# AdminNotesListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**filter_options** | [**AdminNotesListMetaFilterOptions**](AdminNotesListMetaFilterOptions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_notes_list_meta import AdminNotesListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminNotesListMeta from a JSON string
admin_notes_list_meta_instance = AdminNotesListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminNotesListMeta.to_json())

# convert the object into a dict
admin_notes_list_meta_dict = admin_notes_list_meta_instance.to_dict()
# create an instance of AdminNotesListMeta from a dict
admin_notes_list_meta_from_dict = AdminNotesListMeta.from_dict(admin_notes_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


