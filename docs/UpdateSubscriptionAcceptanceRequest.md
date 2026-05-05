# UpdateSubscriptionAcceptanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptance_token** | **str** | Token from the subscription order email | [optional] 
**subscription** | [**UpdateSubscriptionAcceptanceRequestSubscription**](UpdateSubscriptionAcceptanceRequestSubscription.md) |  | 

## Example

```python
from winthrop_client_python.models.update_subscription_acceptance_request import UpdateSubscriptionAcceptanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionAcceptanceRequest from a JSON string
update_subscription_acceptance_request_instance = UpdateSubscriptionAcceptanceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionAcceptanceRequest.to_json())

# convert the object into a dict
update_subscription_acceptance_request_dict = update_subscription_acceptance_request_instance.to_dict()
# create an instance of UpdateSubscriptionAcceptanceRequest from a dict
update_subscription_acceptance_request_from_dict = UpdateSubscriptionAcceptanceRequest.from_dict(update_subscription_acceptance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


