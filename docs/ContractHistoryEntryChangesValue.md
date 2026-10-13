# ContractHistoryEntryChangesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old** | **object** | Value before the change (a JSON scalar, array or object) | 
**new** | **object** | Value after the change (a JSON scalar, array or object) | 

## Example

```python
from winthrop_client_python.models.contract_history_entry_changes_value import ContractHistoryEntryChangesValue

# TODO update the JSON string below
json = "{}"
# create an instance of ContractHistoryEntryChangesValue from a JSON string
contract_history_entry_changes_value_instance = ContractHistoryEntryChangesValue.from_json(json)
# print the JSON string representation of the object
print(ContractHistoryEntryChangesValue.to_json())

# convert the object into a dict
contract_history_entry_changes_value_dict = contract_history_entry_changes_value_instance.to_dict()
# create an instance of ContractHistoryEntryChangesValue from a dict
contract_history_entry_changes_value_from_dict = ContractHistoryEntryChangesValue.from_dict(contract_history_entry_changes_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


