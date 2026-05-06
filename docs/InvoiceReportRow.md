# InvoiceReportRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**invoice_date** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 
**payment_received** | **date** |  | [optional] 
**status** | **str** |  | [optional] 
**amount_dollars** | **object** |  | [optional] 
**notes** | **str** |  | [optional] 
**account** | [**InvoiceReportAccount**](InvoiceReportAccount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.invoice_report_row import InvoiceReportRow

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReportRow from a JSON string
invoice_report_row_instance = InvoiceReportRow.from_json(json)
# print the JSON string representation of the object
print(InvoiceReportRow.to_json())

# convert the object into a dict
invoice_report_row_dict = invoice_report_row_instance.to_dict()
# create an instance of InvoiceReportRow from a dict
invoice_report_row_from_dict = InvoiceReportRow.from_dict(invoice_report_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


