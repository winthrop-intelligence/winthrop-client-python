# AdminInvoiceRowAction

kind: create_invoice (subscription_year_id) | review_and_send (subscription_id, invoice_id) | open_invoice (subscription_id, invoice_id) | open_subscription (subscription_id). The frontend follows this to the matching page/action. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**label** | **str** |  | 
**subscription_id** | **int** |  | [optional] 
**invoice_id** | **int** |  | [optional] 
**subscription_year_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_invoice_row_action import AdminInvoiceRowAction

# TODO update the JSON string below
json = "{}"
# create an instance of AdminInvoiceRowAction from a JSON string
admin_invoice_row_action_instance = AdminInvoiceRowAction.from_json(json)
# print the JSON string representation of the object
print(AdminInvoiceRowAction.to_json())

# convert the object into a dict
admin_invoice_row_action_dict = admin_invoice_row_action_instance.to_dict()
# create an instance of AdminInvoiceRowAction from a dict
admin_invoice_row_action_from_dict = AdminInvoiceRowAction.from_dict(admin_invoice_row_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


