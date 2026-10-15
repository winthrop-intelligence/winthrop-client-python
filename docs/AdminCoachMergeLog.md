# AdminCoachMergeLog


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

## Example

```python
from winthrop_client_python.models.admin_coach_merge_log import AdminCoachMergeLog

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachMergeLog from a JSON string
admin_coach_merge_log_instance = AdminCoachMergeLog.from_json(json)
# print the JSON string representation of the object
print(AdminCoachMergeLog.to_json())

# convert the object into a dict
admin_coach_merge_log_dict = admin_coach_merge_log_instance.to_dict()
# create an instance of AdminCoachMergeLog from a dict
admin_coach_merge_log_from_dict = AdminCoachMergeLog.from_dict(admin_coach_merge_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


