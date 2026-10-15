# AdminCoachMergeLogPreview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_coach** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**duplicate_coach** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**positions** | **List[object]** |  | [optional] 
**compensations** | **List[object]** |  | [optional] 
**income_reports** | **List[object]** |  | [optional] 
**contracts** | **List[object]** |  | [optional] 
**coaches** | **object** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_merge_log_preview import AdminCoachMergeLogPreview

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachMergeLogPreview from a JSON string
admin_coach_merge_log_preview_instance = AdminCoachMergeLogPreview.from_json(json)
# print the JSON string representation of the object
print(AdminCoachMergeLogPreview.to_json())

# convert the object into a dict
admin_coach_merge_log_preview_dict = admin_coach_merge_log_preview_instance.to_dict()
# create an instance of AdminCoachMergeLogPreview from a dict
admin_coach_merge_log_preview_from_dict = AdminCoachMergeLogPreview.from_dict(admin_coach_merge_log_preview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


