# AdminInvoiceFormSettledInvoice

Prefill only. A pending, sent or paid invoice that already bills this subscription year, so the form can warn before a second one is created. Null otherwise.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**state** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_invoice_form_settled_invoice import AdminInvoiceFormSettledInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceFormSettledInvoice from a JSON string
admin_invoice_form_settled_invoice_instance = AdminInvoiceFormSettledInvoice.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceFormSettledInvoice.to_json())

# convert the object into a dict
admin_invoice_form_settled_invoice_dict = admin_invoice_form_settled_invoice_instance.to_dict()
# create an instance of AdminInvoiceFormSettledInvoice from a dict
admin_invoice_form_settled_invoice_from_dict = AdminInvoiceFormSettledInvoice.from_dict(admin_invoice_form_settled_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


