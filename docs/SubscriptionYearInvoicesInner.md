# SubscriptionYearInvoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_year_id** | **int** |  | 
**invoice_id** | **int** |  | 
**state** | **str** |  | 
**sent_at** | **datetime** |  | 
**payment_received** | **datetime** |  | 

## Example

```python
from winthrop_client_python.models.subscription_year_invoices_inner import SubscriptionYearInvoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionYearInvoicesInner from a JSON string
subscription_year_invoices_inner_instance = SubscriptionYearInvoicesInner.from_json(json)
# print the JSON string representation of the object
print(SubscriptionYearInvoicesInner.to_json())

# convert the object into a dict
subscription_year_invoices_inner_dict = subscription_year_invoices_inner_instance.to_dict()
# create an instance of SubscriptionYearInvoicesInner from a dict
subscription_year_invoices_inner_from_dict = SubscriptionYearInvoicesInner.from_dict(subscription_year_invoices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


