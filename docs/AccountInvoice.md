# AccountInvoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**description** | **str** |  | [optional] 
**amount_cents** | **int** |  | [optional] 
**purchase_order_number** | **str** |  | [optional] 
**due_date** | **date** |  | [optional] 
**due_date_notes** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**payment_received** | **date** |  | [optional] 
**status** | **str** |  | [optional] 
**reminders** | **bool** |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**created_by_name** | **str** |  | [optional] 
**can_read** | **bool** | Whether the current user can view this invoice&#39;s PDF | [optional] 

## Example

```python
from winthrop_client_python.models.account_invoice import AccountInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInvoice from a JSON string
account_invoice_instance = AccountInvoice.from_json(json)
# print the JSON string representation of the object
print(AccountInvoice.to_json())

# convert the object into a dict
account_invoice_dict = account_invoice_instance.to_dict()
# create an instance of AccountInvoice from a dict
account_invoice_from_dict = AccountInvoice.from_dict(account_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


