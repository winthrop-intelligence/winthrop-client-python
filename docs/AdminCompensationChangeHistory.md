# AdminCompensationChangeHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminCompensationChangeHistoryDataInner]**](AdminCompensationChangeHistoryDataInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_compensation_change_history import AdminCompensationChangeHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AdminCompensationChangeHistory from a JSON string
admin_compensation_change_history_instance = AdminCompensationChangeHistory.from_json(json)
# print the JSON string representation of the object
print(AdminCompensationChangeHistory.to_json())

# convert the object into a dict
admin_compensation_change_history_dict = admin_compensation_change_history_instance.to_dict()
# create an instance of AdminCompensationChangeHistory from a dict
admin_compensation_change_history_from_dict = AdminCompensationChangeHistory.from_dict(admin_compensation_change_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


