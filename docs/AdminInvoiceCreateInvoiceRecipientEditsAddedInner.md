# AdminInvoiceCreateInvoiceRecipientEditsAddedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | 
**phone** | **str** | Optional. | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_create_invoice_recipient_edits_added_inner import AdminInvoiceCreateInvoiceRecipientEditsAddedInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceCreateInvoiceRecipientEditsAddedInner from a JSON string
admin_invoice_create_invoice_recipient_edits_added_inner_instance = AdminInvoiceCreateInvoiceRecipientEditsAddedInner.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceCreateInvoiceRecipientEditsAddedInner.to_json())

# convert the object into a dict
admin_invoice_create_invoice_recipient_edits_added_inner_dict = admin_invoice_create_invoice_recipient_edits_added_inner_instance.to_dict()
# create an instance of AdminInvoiceCreateInvoiceRecipientEditsAddedInner from a dict
admin_invoice_create_invoice_recipient_edits_added_inner_from_dict = AdminInvoiceCreateInvoiceRecipientEditsAddedInner.from_dict(admin_invoice_create_invoice_recipient_edits_added_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


