# ContractHistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** |  | 
**item_id** | **int** |  | 
**event** | **str** |  | 
**changes** | [**Dict[str, ContractHistoryEntryChangesValue]**](ContractHistoryEntryChangesValue.md) | Every changed field with its old and new value. A create has no old values (old is null); for a destroy the old values are the row as it was deleted and new is null. Empty when the stored version cannot be read (then &#x60;changes_unreadable&#x60; is true) and also for a version that recorded no field change. | 
**changes_unreadable** | **bool** | True only when the stored version data could not be read, so &#x60;changes&#x60; is empty because of that and not because nothing changed. False for every readable version, including one that recorded no field change. | 
**user** | [**ContractHistoryEntryUser**](ContractHistoryEntryUser.md) |  | 
**oauth_application** | [**ContractHistoryEntryOauthApplication**](ContractHistoryEntryOauthApplication.md) |  | 
**created_at** | **datetime** |  | 
**change_note** | **str** | Why the API write was made, as the caller gave it; null for edits made without one (such as the admin UI). | 

## Example

```python
from winthrop_client_python.models.contract_history_entry import ContractHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ContractHistoryEntry from a JSON string
contract_history_entry_instance = ContractHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(ContractHistoryEntry.to_json())

# convert the object into a dict
contract_history_entry_dict = contract_history_entry_instance.to_dict()
# create an instance of ContractHistoryEntry from a dict
contract_history_entry_from_dict = ContractHistoryEntry.from_dict(contract_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


