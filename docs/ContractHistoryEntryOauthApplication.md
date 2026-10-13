# ContractHistoryEntryOauthApplication

The API client of a write made through the API; null for admin-UI, job and console edits.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**consumer_key** | **str** |  | 

## Example

```python
from winthrop_client_python.models.contract_history_entry_oauth_application import ContractHistoryEntryOauthApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ContractHistoryEntryOauthApplication from a JSON string
contract_history_entry_oauth_application_instance = ContractHistoryEntryOauthApplication.from_json(json)
# print the JSON string representation of the object
print(ContractHistoryEntryOauthApplication.to_json())

# convert the object into a dict
contract_history_entry_oauth_application_dict = contract_history_entry_oauth_application_instance.to_dict()
# create an instance of ContractHistoryEntryOauthApplication from a dict
contract_history_entry_oauth_application_from_dict = ContractHistoryEntryOauthApplication.from_dict(contract_history_entry_oauth_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


