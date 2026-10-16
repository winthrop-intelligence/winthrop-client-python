# UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**year_number** | **int** |  | [optional] 
**service_start** | **date** |  | [optional] 
**service_end** | **date** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**due_date** | **date** |  | [optional] 
**destroy** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_subscription_request_subscription_subscription_years_attributes_inner import UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner from a JSON string
update_subscription_request_subscription_subscription_years_attributes_inner_instance = UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.to_json())

# convert the object into a dict
update_subscription_request_subscription_subscription_years_attributes_inner_dict = update_subscription_request_subscription_subscription_years_attributes_inner_instance.to_dict()
# create an instance of UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner from a dict
update_subscription_request_subscription_subscription_years_attributes_inner_from_dict = UpdateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.from_dict(update_subscription_request_subscription_subscription_years_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


