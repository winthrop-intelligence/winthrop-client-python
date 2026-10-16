# AdminIncomeReportRawContractSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**filename** | **str** |  | [optional] 
**pdf_preview_url** | **str** |  | [optional] 
**pdf_download_url** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_income_report_raw_contract_summary import AdminIncomeReportRawContractSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminIncomeReportRawContractSummary from a JSON string
admin_income_report_raw_contract_summary_instance = AdminIncomeReportRawContractSummary.from_json(json)
# print the JSON string representation of the object
print(AdminIncomeReportRawContractSummary.to_json())

# convert the object into a dict
admin_income_report_raw_contract_summary_dict = admin_income_report_raw_contract_summary_instance.to_dict()
# create an instance of AdminIncomeReportRawContractSummary from a dict
admin_income_report_raw_contract_summary_from_dict = AdminIncomeReportRawContractSummary.from_dict(admin_income_report_raw_contract_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


