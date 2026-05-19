# InvoiceReportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 
**invoices** | [**List[InvoiceReportRow]**](InvoiceReportRow.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.invoice_report_result import InvoiceReportResult

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReportResult from a JSON string
invoice_report_result_instance = InvoiceReportResult.from_json(json)
# print the JSON string representation of the object
print(InvoiceReportResult.to_json())

# convert the object into a dict
invoice_report_result_dict = invoice_report_result_instance.to_dict()
# create an instance of InvoiceReportResult from a dict
invoice_report_result_from_dict = InvoiceReportResult.from_dict(invoice_report_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


