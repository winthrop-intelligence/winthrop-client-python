# AdminCoachMergeLogListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**filter_options** | [**AdminCoachMergeLogListMetaFilterOptions**](AdminCoachMergeLogListMetaFilterOptions.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_merge_log_list_meta import AdminCoachMergeLogListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachMergeLogListMeta from a JSON string
admin_coach_merge_log_list_meta_instance = AdminCoachMergeLogListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminCoachMergeLogListMeta.to_json())

# convert the object into a dict
admin_coach_merge_log_list_meta_dict = admin_coach_merge_log_list_meta_instance.to_dict()
# create an instance of AdminCoachMergeLogListMeta from a dict
admin_coach_merge_log_list_meta_from_dict = AdminCoachMergeLogListMeta.from_dict(admin_coach_merge_log_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


