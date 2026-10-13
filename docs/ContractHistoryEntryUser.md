# ContractHistoryEntryUser

Who made the change; null when none was recorded. A user deleted since keeps the id with a null name.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.contract_history_entry_user import ContractHistoryEntryUser

# TODO update the JSON string below
json = "{}"
# create an instance of ContractHistoryEntryUser from a JSON string
contract_history_entry_user_instance = ContractHistoryEntryUser.from_json(json)
# print the JSON string representation of the object
print(ContractHistoryEntryUser.to_json())

# convert the object into a dict
contract_history_entry_user_dict = contract_history_entry_user_instance.to_dict()
# create an instance of ContractHistoryEntryUser from a dict
contract_history_entry_user_from_dict = ContractHistoryEntryUser.from_dict(contract_history_entry_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


