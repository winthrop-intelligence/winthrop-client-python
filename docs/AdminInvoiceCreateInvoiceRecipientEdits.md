# AdminInvoiceCreateInvoiceRecipientEdits

What the operator changed in the prefilled recipient list. Omitted, the invoice goes to the account's current contacts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**removed** | **List[str]** | Contact emails to leave off, matched case-insensitively. | [optional] 
**added** | [**List[AdminInvoiceCreateInvoiceRecipientEditsAddedInner]**](AdminInvoiceCreateInvoiceRecipientEditsAddedInner.md) | Recipients to add. One whose email (case-insensitively) is already on the invoice is skipped. | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_create_invoice_recipient_edits import AdminInvoiceCreateInvoiceRecipientEdits

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceCreateInvoiceRecipientEdits from a JSON string
admin_invoice_create_invoice_recipient_edits_instance = AdminInvoiceCreateInvoiceRecipientEdits.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceCreateInvoiceRecipientEdits.to_json())

# convert the object into a dict
admin_invoice_create_invoice_recipient_edits_dict = admin_invoice_create_invoice_recipient_edits_instance.to_dict()
# create an instance of AdminInvoiceCreateInvoiceRecipientEdits from a dict
admin_invoice_create_invoice_recipient_edits_from_dict = AdminInvoiceCreateInvoiceRecipientEdits.from_dict(admin_invoice_create_invoice_recipient_edits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


