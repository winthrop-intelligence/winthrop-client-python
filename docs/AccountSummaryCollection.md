# AccountSummaryCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccountSummary]**](AccountSummary.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.account_summary_collection import AccountSummaryCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSummaryCollection from a JSON string
account_summary_collection_instance = AccountSummaryCollection.from_json(json)
# print the JSON string representation of the object
print(AccountSummaryCollection.to_json())

# convert the object into a dict
account_summary_collection_dict = account_summary_collection_instance.to_dict()
# create an instance of AccountSummaryCollection from a dict
account_summary_collection_from_dict = AccountSummaryCollection.from_dict(account_summary_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


