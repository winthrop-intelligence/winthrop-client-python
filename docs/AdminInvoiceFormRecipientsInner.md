# AdminInvoiceFormRecipientsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** | Optional. | 

## Example

```python
from winthrop_client_python.models.admin_invoice_form_recipients_inner import AdminInvoiceFormRecipientsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceFormRecipientsInner from a JSON string
admin_invoice_form_recipients_inner_instance = AdminInvoiceFormRecipientsInner.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceFormRecipientsInner.to_json())

# convert the object into a dict
admin_invoice_form_recipients_inner_dict = admin_invoice_form_recipients_inner_instance.to_dict()
# create an instance of AdminInvoiceFormRecipientsInner from a dict
admin_invoice_form_recipients_inner_from_dict = AdminInvoiceFormRecipientsInner.from_dict(admin_invoice_form_recipients_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


