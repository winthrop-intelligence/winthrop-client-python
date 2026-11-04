# AdminIncomeReport

An outside income report for a coach

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**coach_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**contract_status_id** | **int** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**outside_income_cents** | **int** | Total athletically related cash income the form reports, in cents. 0 when the form says no income; null when not read yet. | [optional] 
**reported_period** | **str** | The period exactly as the form states it. Null when not read. | [optional] 
**label** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**coach** | [**AdminIncomeReportCoachSummary**](AdminIncomeReportCoachSummary.md) |  | [optional] 
**contract_status** | [**AdminIncomeReportContractStatusSummary**](AdminIncomeReportContractStatusSummary.md) |  | [optional] 
**raw_contract** | [**AdminIncomeReportRawContractSummary**](AdminIncomeReportRawContractSummary.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_income_report import AdminIncomeReport

# TODO update the JSON string below
json = "{}"
# create an instance of AdminIncomeReport from a JSON string
admin_income_report_instance = AdminIncomeReport.from_json(json)
# print the JSON string representation of the object
print(AdminIncomeReport.to_json())

# convert the object into a dict
admin_income_report_dict = admin_income_report_instance.to_dict()
# create an instance of AdminIncomeReport from a dict
admin_income_report_from_dict = AdminIncomeReport.from_dict(admin_income_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


