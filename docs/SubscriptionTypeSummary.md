# SubscriptionTypeSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**name_display** | **str** |  | 
**free** | **bool** | Whether this is the FREE subscription type. | 

## Example

```python
from winthrop_client_python.models.subscription_type_summary import SubscriptionTypeSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionTypeSummary from a JSON string
subscription_type_summary_instance = SubscriptionTypeSummary.from_json(json)
# print the JSON string representation of the object
print(SubscriptionTypeSummary.to_json())

# convert the object into a dict
subscription_type_summary_dict = subscription_type_summary_instance.to_dict()
# create an instance of SubscriptionTypeSummary from a dict
subscription_type_summary_from_dict = SubscriptionTypeSummary.from_dict(subscription_type_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


