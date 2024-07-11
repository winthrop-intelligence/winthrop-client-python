# SubscriptionCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Subscription]**](Subscription.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.subscription_collection import SubscriptionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionCollection from a JSON string
subscription_collection_instance = SubscriptionCollection.from_json(json)
# print the JSON string representation of the object
print(SubscriptionCollection.to_json())

# convert the object into a dict
subscription_collection_dict = subscription_collection_instance.to_dict()
# create an instance of SubscriptionCollection from a dict
subscription_collection_form_dict = subscription_collection.from_dict(subscription_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


