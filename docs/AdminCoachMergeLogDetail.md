# AdminCoachMergeLogDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**primary_coach_id** | **int** |  | [optional] 
**duplicate_coach_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**user** | [**ContactSearchCoachOptionsCoachesInner**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**positions** | **List[object]** |  | [optional] 
**compensations** | **List[object]** |  | [optional] 
**contracts** | **List[object]** |  | [optional] 
**income_reports** | **List[object]** |  | [optional] 
**coaches** | [**AdminCoachMergeLogDetailAllOfCoaches**](AdminCoachMergeLogDetailAllOfCoaches.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_merge_log_detail import AdminCoachMergeLogDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachMergeLogDetail from a JSON string
admin_coach_merge_log_detail_instance = AdminCoachMergeLogDetail.from_json(json)
# print the JSON string representation of the object
print(AdminCoachMergeLogDetail.to_json())

# convert the object into a dict
admin_coach_merge_log_detail_dict = admin_coach_merge_log_detail_instance.to_dict()
# create an instance of AdminCoachMergeLogDetail from a dict
admin_coach_merge_log_detail_from_dict = AdminCoachMergeLogDetail.from_dict(admin_coach_merge_log_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


