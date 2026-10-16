# AdminIncomeReportContractStatusSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_income_report_contract_status_summary import AdminIncomeReportContractStatusSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminIncomeReportContractStatusSummary from a JSON string
admin_income_report_contract_status_summary_instance = AdminIncomeReportContractStatusSummary.from_json(json)
# print the JSON string representation of the object
print(AdminIncomeReportContractStatusSummary.to_json())

# convert the object into a dict
admin_income_report_contract_status_summary_dict = admin_income_report_contract_status_summary_instance.to_dict()
# create an instance of AdminIncomeReportContractStatusSummary from a dict
admin_income_report_contract_status_summary_from_dict = AdminIncomeReportContractStatusSummary.from_dict(admin_income_report_contract_status_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


