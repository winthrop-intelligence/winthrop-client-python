# SubscriptionChangeHistoryPageMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | 
**total_pages** | **int** |  | 
**total_entries** | **int** |  | 
**next_page** | **int** |  | 
**previous_page** | **int** |  | 

## Example

```python
from winthrop_client_python.models.subscription_change_history_page_meta import SubscriptionChangeHistoryPageMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionChangeHistoryPageMeta from a JSON string
subscription_change_history_page_meta_instance = SubscriptionChangeHistoryPageMeta.from_json(json)
# print the JSON string representation of the object
print(SubscriptionChangeHistoryPageMeta.to_json())

# convert the object into a dict
subscription_change_history_page_meta_dict = subscription_change_history_page_meta_instance.to_dict()
# create an instance of SubscriptionChangeHistoryPageMeta from a dict
subscription_change_history_page_meta_from_dict = SubscriptionChangeHistoryPageMeta.from_dict(subscription_change_history_page_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


