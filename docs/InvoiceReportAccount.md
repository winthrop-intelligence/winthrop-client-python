# InvoiceReportAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.invoice_report_account import InvoiceReportAccount

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReportAccount from a JSON string
invoice_report_account_instance = InvoiceReportAccount.from_json(json)
# print the JSON string representation of the object
print(InvoiceReportAccount.to_json())

# convert the object into a dict
invoice_report_account_dict = invoice_report_account_instance.to_dict()
# create an instance of InvoiceReportAccount from a dict
invoice_report_account_from_dict = InvoiceReportAccount.from_dict(invoice_report_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


