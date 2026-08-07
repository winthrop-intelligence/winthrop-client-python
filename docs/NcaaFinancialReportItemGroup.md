# NcaaFinancialReportItemGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**section** | **str** |  | 
**items** | [**List[NcaaFinancialReportItemValue]**](NcaaFinancialReportItemValue.md) |  | 

## Example

```python
from winthrop_client_python.models.ncaa_financial_report_item_group import NcaaFinancialReportItemGroup

# TODO update the JSON string below
json = "{}"
# create an instance of NcaaFinancialReportItemGroup from a JSON string
ncaa_financial_report_item_group_instance = NcaaFinancialReportItemGroup.from_json(json)
# print the JSON string representation of the object
print(NcaaFinancialReportItemGroup.to_json())

# convert the object into a dict
ncaa_financial_report_item_group_dict = ncaa_financial_report_item_group_instance.to_dict()
# create an instance of NcaaFinancialReportItemGroup from a dict
ncaa_financial_report_item_group_from_dict = NcaaFinancialReportItemGroup.from_dict(ncaa_financial_report_item_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


