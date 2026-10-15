# AdminCoachMergeLogListMetaFilterOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[IdName]**](IdName.md) |  | [optional] 
**statuses** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_merge_log_list_meta_filter_options import AdminCoachMergeLogListMetaFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachMergeLogListMetaFilterOptions from a JSON string
admin_coach_merge_log_list_meta_filter_options_instance = AdminCoachMergeLogListMetaFilterOptions.from_json(json)
# print the JSON string representation of the object
print(AdminCoachMergeLogListMetaFilterOptions.to_json())

# convert the object into a dict
admin_coach_merge_log_list_meta_filter_options_dict = admin_coach_merge_log_list_meta_filter_options_instance.to_dict()
# create an instance of AdminCoachMergeLogListMetaFilterOptions from a dict
admin_coach_merge_log_list_meta_filter_options_from_dict = AdminCoachMergeLogListMetaFilterOptions.from_dict(admin_coach_merge_log_list_meta_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


