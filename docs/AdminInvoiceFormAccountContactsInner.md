# AdminInvoiceFormAccountContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_invoice_form_account_contacts_inner import AdminInvoiceFormAccountContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceFormAccountContactsInner from a JSON string
admin_invoice_form_account_contacts_inner_instance = AdminInvoiceFormAccountContactsInner.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceFormAccountContactsInner.to_json())

# convert the object into a dict
admin_invoice_form_account_contacts_inner_dict = admin_invoice_form_account_contacts_inner_instance.to_dict()
# create an instance of AdminInvoiceFormAccountContactsInner from a dict
admin_invoice_form_account_contacts_inner_from_dict = AdminInvoiceFormAccountContactsInner.from_dict(admin_invoice_form_account_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


