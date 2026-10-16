# AdminInvoicesResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**not_sent_count** | **int** | Total Not-sent rows regardless of the active tab — backs the \&quot;N not sent\&quot; count. | [optional] 
**invoices_count** | **int** | Every invoice in the system whatever the filters, the \&quot;318\&quot; of \&quot;318 invoices · 5 shown\&quot;. | [optional] 
**totals** | [**AdminInvoicesResponseMetaTotals**](AdminInvoicesResponseMetaTotals.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoices_response_meta import AdminInvoicesResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoicesResponseMeta from a JSON string
admin_invoices_response_meta_instance = AdminInvoicesResponseMeta.from_json(json)
# print the JSON string representation of the object
print(AdminInvoicesResponseMeta.to_json())

# convert the object into a dict
admin_invoices_response_meta_dict = admin_invoices_response_meta_instance.to_dict()
# create an instance of AdminInvoicesResponseMeta from a dict
admin_invoices_response_meta_from_dict = AdminInvoicesResponseMeta.from_dict(admin_invoices_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


