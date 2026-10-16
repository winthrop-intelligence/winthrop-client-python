# CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year_number** | **int** |  | [optional] 
**service_start** | **date** |  | [optional] 
**service_end** | **date** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**due_date** | **date** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_subscription_request_subscription_subscription_years_attributes_inner import CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner from a JSON string
create_subscription_request_subscription_subscription_years_attributes_inner_instance = CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.to_json())

# convert the object into a dict
create_subscription_request_subscription_subscription_years_attributes_inner_dict = create_subscription_request_subscription_subscription_years_attributes_inner_instance.to_dict()
# create an instance of CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner from a dict
create_subscription_request_subscription_subscription_years_attributes_inner_from_dict = CreateSubscriptionRequestSubscriptionSubscriptionYearsAttributesInner.from_dict(create_subscription_request_subscription_subscription_years_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


