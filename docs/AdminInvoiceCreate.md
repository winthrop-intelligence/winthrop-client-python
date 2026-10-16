# AdminInvoiceCreate

A new invoice always starts from a schedule year. Its recipients are the account's invoice contacts as they are when it is saved, with the form's recipient_edits applied, so a contact who changed while the form was open is not copied onto it. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**AdminInvoiceCreateInvoice**](AdminInvoiceCreateInvoice.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_create import AdminInvoiceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceCreate from a JSON string
admin_invoice_create_instance = AdminInvoiceCreate.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceCreate.to_json())

# convert the object into a dict
admin_invoice_create_dict = admin_invoice_create_instance.to_dict()
# create an instance of AdminInvoiceCreate from a dict
admin_invoice_create_from_dict = AdminInvoiceCreate.from_dict(admin_invoice_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


