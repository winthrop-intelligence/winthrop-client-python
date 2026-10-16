# AdminInvoiceWriteInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_year_id** | **int** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**due_date** | **date** |  | [optional] 
**due_date_notes** | **str** |  | [optional] 
**purchase_order_number** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**reminders** | **bool** |  | [optional] 
**billing_addresses_attributes** | [**List[AdminInvoiceWriteInvoiceBillingAddressesAttributesInner]**](AdminInvoiceWriteInvoiceBillingAddressesAttributesInner.md) | Changes to the invoice&#39;s recipients: &#x60;{id, _destroy: true}&#x60; removes one, &#x60;{first_name, last_name, email}&#x60; adds one. | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_write_invoice import AdminInvoiceWriteInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceWriteInvoice from a JSON string
admin_invoice_write_invoice_instance = AdminInvoiceWriteInvoice.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceWriteInvoice.to_json())

# convert the object into a dict
admin_invoice_write_invoice_dict = admin_invoice_write_invoice_instance.to_dict()
# create an instance of AdminInvoiceWriteInvoice from a dict
admin_invoice_write_invoice_from_dict = AdminInvoiceWriteInvoice.from_dict(admin_invoice_write_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


