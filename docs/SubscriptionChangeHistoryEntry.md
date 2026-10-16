# SubscriptionChangeHistoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The audit version id. | 
**occurred_at** | **datetime** |  | 
**occurred_at_label** | **str** | The same moment as readable text in UTC, or Unknown time. | 
**actor** | **str** | A name and email, an email, System when no user made the change, or Unknown. | 
**record_label** | **str** | The record the change was made to. | 
**event_label** | **str** | Created or Deleted for the creation or deletion of a record, empty on an update. | [optional] 
**changes** | [**List[SubscriptionChangeHistoryChange]**](SubscriptionChangeHistoryChange.md) | Empty on a deletion. | 

## Example

```python
from winthrop_client_python.models.subscription_change_history_entry import SubscriptionChangeHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionChangeHistoryEntry from a JSON string
subscription_change_history_entry_instance = SubscriptionChangeHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(SubscriptionChangeHistoryEntry.to_json())

# convert the object into a dict
subscription_change_history_entry_dict = subscription_change_history_entry_instance.to_dict()
# create an instance of SubscriptionChangeHistoryEntry from a dict
subscription_change_history_entry_from_dict = SubscriptionChangeHistoryEntry.from_dict(subscription_change_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


