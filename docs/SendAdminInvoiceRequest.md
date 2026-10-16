# SendAdminInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Overrides the templated email body for this send (see &#x60;default_message&#x60;). | [optional] 
**resend** | **bool** | A deliberate Resend of an already-sent invoice. Without it, sending a sent invoice is treated as a duplicate and refused. A resend within a minute of the last send is also refused, so a double click sends once. | [optional] 

## Example

```python
from winthrop_client_python.models.send_admin_invoice_request import SendAdminInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendAdminInvoiceRequest from a JSON string
send_admin_invoice_request_instance = SendAdminInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(SendAdminInvoiceRequest.to_json())

# convert the object into a dict
send_admin_invoice_request_dict = send_admin_invoice_request_instance.to_dict()
# create an instance of SendAdminInvoiceRequest from a dict
send_admin_invoice_request_from_dict = SendAdminInvoiceRequest.from_dict(send_admin_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


