# UpdateSubscriptionAcceptanceRequestSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract_term** | **int** |  | 
**contract_accepted** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.update_subscription_acceptance_request_subscription import UpdateSubscriptionAcceptanceRequestSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionAcceptanceRequestSubscription from a JSON string
update_subscription_acceptance_request_subscription_instance = UpdateSubscriptionAcceptanceRequestSubscription.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionAcceptanceRequestSubscription.to_json())

# convert the object into a dict
update_subscription_acceptance_request_subscription_dict = update_subscription_acceptance_request_subscription_instance.to_dict()
# create an instance of UpdateSubscriptionAcceptanceRequestSubscription from a dict
update_subscription_acceptance_request_subscription_from_dict = UpdateSubscriptionAcceptanceRequestSubscription.from_dict(update_subscription_acceptance_request_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


