# AdminInvoicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminInvoicesResponseMeta**](AdminInvoicesResponseMeta.md) |  | 
**data** | [**List[AdminInvoiceRow]**](AdminInvoiceRow.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_invoices_response import AdminInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoicesResponse from a JSON string
admin_invoices_response_instance = AdminInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(AdminInvoicesResponse.to_json())

# convert the object into a dict
admin_invoices_response_dict = admin_invoices_response_instance.to_dict()
# create an instance of AdminInvoicesResponse from a dict
admin_invoices_response_from_dict = AdminInvoicesResponse.from_dict(admin_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


