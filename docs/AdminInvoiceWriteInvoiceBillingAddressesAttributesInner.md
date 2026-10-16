# AdminInvoiceWriteInvoiceBillingAddressesAttributesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**destroy** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** | Optional. | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_write_invoice_billing_addresses_attributes_inner import AdminInvoiceWriteInvoiceBillingAddressesAttributesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceWriteInvoiceBillingAddressesAttributesInner from a JSON string
admin_invoice_write_invoice_billing_addresses_attributes_inner_instance = AdminInvoiceWriteInvoiceBillingAddressesAttributesInner.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceWriteInvoiceBillingAddressesAttributesInner.to_json())

# convert the object into a dict
admin_invoice_write_invoice_billing_addresses_attributes_inner_dict = admin_invoice_write_invoice_billing_addresses_attributes_inner_instance.to_dict()
# create an instance of AdminInvoiceWriteInvoiceBillingAddressesAttributesInner from a dict
admin_invoice_write_invoice_billing_addresses_attributes_inner_from_dict = AdminInvoiceWriteInvoiceBillingAddressesAttributesInner.from_dict(admin_invoice_write_invoice_billing_addresses_attributes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


