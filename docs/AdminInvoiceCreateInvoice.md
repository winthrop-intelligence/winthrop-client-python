# AdminInvoiceCreateInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_year_id** | **int** |  | 
**invoice_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**due_date** | **date** |  | [optional] 
**due_date_notes** | **str** |  | [optional] 
**purchase_order_number** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**reminders** | **bool** |  | [optional] 
**recipient_edits** | [**AdminInvoiceCreateInvoiceRecipientEdits**](AdminInvoiceCreateInvoiceRecipientEdits.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_create_invoice import AdminInvoiceCreateInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceCreateInvoice from a JSON string
admin_invoice_create_invoice_instance = AdminInvoiceCreateInvoice.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceCreateInvoice.to_json())

# convert the object into a dict
admin_invoice_create_invoice_dict = admin_invoice_create_invoice_instance.to_dict()
# create an instance of AdminInvoiceCreateInvoice from a dict
admin_invoice_create_invoice_from_dict = AdminInvoiceCreateInvoice.from_dict(admin_invoice_create_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


