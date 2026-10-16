# AdminInvoiceFormServicePeriodsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The subscription_year id. | 
**year_number** | **int** |  | 
**service_start** | **date** |  | 
**service_end** | **date** |  | 

## Example

```python
from winthrop_client_python.models.admin_invoice_form_service_periods_inner import AdminInvoiceFormServicePeriodsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceFormServicePeriodsInner from a JSON string
admin_invoice_form_service_periods_inner_instance = AdminInvoiceFormServicePeriodsInner.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceFormServicePeriodsInner.to_json())

# convert the object into a dict
admin_invoice_form_service_periods_inner_dict = admin_invoice_form_service_periods_inner_instance.to_dict()
# create an instance of AdminInvoiceFormServicePeriodsInner from a dict
admin_invoice_form_service_periods_inner_from_dict = AdminInvoiceFormServicePeriodsInner.from_dict(admin_invoice_form_service_periods_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


