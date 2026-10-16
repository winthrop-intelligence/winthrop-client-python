# AdminInvoiceWrite

PATCH accepts subscription_year_id to move the invoice to another year of the same subscription; a year from any other subscription, or one that no longer exists, is refused with 422. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**AdminInvoiceWriteInvoice**](AdminInvoiceWriteInvoice.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_write import AdminInvoiceWrite

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceWrite from a JSON string
admin_invoice_write_instance = AdminInvoiceWrite.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceWrite.to_json())

# convert the object into a dict
admin_invoice_write_dict = admin_invoice_write_instance.to_dict()
# create an instance of AdminInvoiceWrite from a dict
admin_invoice_write_from_dict = AdminInvoiceWrite.from_dict(admin_invoice_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


