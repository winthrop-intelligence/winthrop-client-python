# AdminCoachMergeLogList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminCoachMergeLogListMeta**](AdminCoachMergeLogListMeta.md) |  | [optional] 
**data** | [**List[AdminCoachMergeLog]**](AdminCoachMergeLog.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_coach_merge_log_list import AdminCoachMergeLogList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCoachMergeLogList from a JSON string
admin_coach_merge_log_list_instance = AdminCoachMergeLogList.from_json(json)
# print the JSON string representation of the object
print(AdminCoachMergeLogList.to_json())

# convert the object into a dict
admin_coach_merge_log_list_dict = admin_coach_merge_log_list_instance.to_dict()
# create an instance of AdminCoachMergeLogList from a dict
admin_coach_merge_log_list_from_dict = AdminCoachMergeLogList.from_dict(admin_coach_merge_log_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


