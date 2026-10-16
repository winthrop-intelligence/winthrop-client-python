# AdminInvoiceFormHints

\"From schedule: …\" text per field, null where there is nothing to say.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_date** | **str** |  | 
**description** | **str** |  | 
**amount_cents** | **str** | Where the suggested amount comes from. A prorated legacy year names its annual rate and months; an ambiguous one starts with \&quot;Check the agreement\&quot;. | 
**due_date** | **str** |  | 
**due_date_notes** | **str** |  | 
**purchase_order_number** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_invoice_form_hints import AdminInvoiceFormHints

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceFormHints from a JSON string
admin_invoice_form_hints_instance = AdminInvoiceFormHints.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceFormHints.to_json())

# convert the object into a dict
admin_invoice_form_hints_dict = admin_invoice_form_hints_instance.to_dict()
# create an instance of AdminInvoiceFormHints from a dict
admin_invoice_form_hints_from_dict = AdminInvoiceFormHints.from_dict(admin_invoice_form_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


