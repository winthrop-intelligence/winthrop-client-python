# AdminCompensationChangeHistoryDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**event** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**user_name** | **str** |  | [optional] 
**change_note** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**changes** | [**List[AdminCompensationChangeHistoryDataInnerChangesInner]**](AdminCompensationChangeHistoryDataInnerChangesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation_change_history_data_inner import AdminCompensationChangeHistoryDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensationChangeHistoryDataInner from a JSON string
admin_compensation_change_history_data_inner_instance = AdminCompensationChangeHistoryDataInner.from_json(json)
# print the JSON string representation of the object
print(AdminCompensationChangeHistoryDataInner.to_json())

# convert the object into a dict
admin_compensation_change_history_data_inner_dict = admin_compensation_change_history_data_inner_instance.to_dict()
# create an instance of AdminCompensationChangeHistoryDataInner from a dict
admin_compensation_change_history_data_inner_from_dict = AdminCompensationChangeHistoryDataInner.from_dict(admin_compensation_change_history_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


