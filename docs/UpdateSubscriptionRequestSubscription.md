# UpdateSubscriptionRequestSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**subscription_type_id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**send_renewal** | **bool** |  | [optional] 
**subscription_years_attributes** | [**List[UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner]**](UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_subscription_request_subscription import UpdateSubscriptionRequestSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionRequestSubscription from a JSON string
update_subscription_request_subscription_instance = UpdateSubscriptionRequestSubscription.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionRequestSubscription.to_json())

# convert the object into a dict
update_subscription_request_subscription_dict = update_subscription_request_subscription_instance.to_dict()
# create an instance of UpdateSubscriptionRequestSubscription from a dict
update_subscription_request_subscription_from_dict = UpdateSubscriptionRequestSubscription.from_dict(update_subscription_request_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


