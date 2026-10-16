# SubscriptionChangeHistoryChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**var_from** | **str** | The earlier value as text, absent on a creation. | [optional] 
**to** | **str** |  | 
**text** | **str** | The whole change in plain English. | 

## Example

```python
from winthrop_client_python.models.subscription_change_history_change import SubscriptionChangeHistoryChange

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionChangeHistoryChange from a JSON string
subscription_change_history_change_instance = SubscriptionChangeHistoryChange.from_json(json)
# print the JSON string representation of the object
print(SubscriptionChangeHistoryChange.to_json())

# convert the object into a dict
subscription_change_history_change_dict = subscription_change_history_change_instance.to_dict()
# create an instance of SubscriptionChangeHistoryChange from a dict
subscription_change_history_change_from_dict = SubscriptionChangeHistoryChange.from_dict(subscription_change_history_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


