# SubscriptionAcceptanceErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** |  | [optional] 
**accepted** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.subscription_acceptance_errors import SubscriptionAcceptanceErrors

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionAcceptanceErrors from a JSON string
subscription_acceptance_errors_instance = SubscriptionAcceptanceErrors.from_json(json)
# print the JSON string representation of the object
print(SubscriptionAcceptanceErrors.to_json())

# convert the object into a dict
subscription_acceptance_errors_dict = subscription_acceptance_errors_instance.to_dict()
# create an instance of SubscriptionAcceptanceErrors from a dict
subscription_acceptance_errors_from_dict = SubscriptionAcceptanceErrors.from_dict(subscription_acceptance_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


