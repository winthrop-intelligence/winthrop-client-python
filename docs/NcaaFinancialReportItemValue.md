# NcaaFinancialReportItemValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_number** | **str** |  | 
**line_item** | **str** |  | 
**section** | **str** |  | 
**value_kind** | **str** |  | 
**raw_value** | **str** |  | 
**numeric_value** | **str** | Exact decimal representation for currency and decimal values. | [optional] 
**text_value** | **str** |  | [optional] 
**reporting_status** | **str** |  | 
**display_value** | **str** |  | 
**position** | **int** |  | 

## Example

```python
from winthrop_client_python.models.ncaa_financial_report_item_value import NcaaFinancialReportItemValue

# TODO update the JSON string below
json = "{}"
# create an instance of NcaaFinancialReportItemValue from a JSON string
ncaa_financial_report_item_value_instance = NcaaFinancialReportItemValue.from_json(json)
# print the JSON string representation of the object
print(NcaaFinancialReportItemValue.to_json())

# convert the object into a dict
ncaa_financial_report_item_value_dict = ncaa_financial_report_item_value_instance.to_dict()
# create an instance of NcaaFinancialReportItemValue from a dict
ncaa_financial_report_item_value_from_dict = NcaaFinancialReportItemValue.from_dict(ncaa_financial_report_item_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


