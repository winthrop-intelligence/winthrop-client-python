# CreateSubscriptionRequestSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | [optional] 
**subscription_type_id** | **int** |  | [optional] 
**start_at** | **date** |  | [optional] 
**end_at** | **date** |  | [optional] 
**active** | **bool** | Whether this subscription grants access immediately. FREE subscriptions are always active. | [optional] [default to True]
**renewal** | **bool** | Whether this agreement renews an existing subscription, independently of immediate activation. | [optional] [default to False]
**notes** | **str** |  | [optional] 
**autorenew** | **bool** |  | [optional] 
**send_renewal** | **bool** |  | [optional] 
**subscription_years_attributes** | [**List[CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner]**](CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_subscription_request_subscription import CreateSubscriptionRequestSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequestSubscription from a JSON string
create_subscription_request_subscription_instance = CreateSubscriptionRequestSubscription.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionRequestSubscription.to_json())

# convert the object into a dict
create_subscription_request_subscription_dict = create_subscription_request_subscription_instance.to_dict()
# create an instance of CreateSubscriptionRequestSubscription from a dict
create_subscription_request_subscription_from_dict = CreateSubscriptionRequestSubscription.from_dict(create_subscription_request_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


