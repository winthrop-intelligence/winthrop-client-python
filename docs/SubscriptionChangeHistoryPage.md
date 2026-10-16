# SubscriptionChangeHistoryPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**SubscriptionChangeHistoryPageMeta**](SubscriptionChangeHistoryPageMeta.md) |  | 
**data** | [**List[SubscriptionChangeHistoryEntry]**](SubscriptionChangeHistoryEntry.md) |  | 

## Example

```python
from winthrop_client_python.models.subscription_change_history_page import SubscriptionChangeHistoryPage

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionChangeHistoryPage from a JSON string
subscription_change_history_page_instance = SubscriptionChangeHistoryPage.from_json(json)
# print the JSON string representation of the object
print(SubscriptionChangeHistoryPage.to_json())

# convert the object into a dict
subscription_change_history_page_dict = subscription_change_history_page_instance.to_dict()
# create an instance of SubscriptionChangeHistoryPage from a dict
subscription_change_history_page_from_dict = SubscriptionChangeHistoryPage.from_dict(subscription_change_history_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


