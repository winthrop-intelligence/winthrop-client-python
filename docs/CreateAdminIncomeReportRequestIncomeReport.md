# CreateAdminIncomeReportRequestIncomeReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach_id** | **int** |  | [optional] 
**year** | **int** |  | [optional] 
**contract_status_id** | **int** |  | [optional] 
**income_report_text** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_income_report_request_income_report import CreateAdminIncomeReportRequestIncomeReport

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminIncomeReportRequestIncomeReport from a JSON string
create_admin_income_report_request_income_report_instance = CreateAdminIncomeReportRequestIncomeReport.from_json(json)
# print the JSON string representation of the object
print(CreateAdminIncomeReportRequestIncomeReport.to_json())

# convert the object into a dict
create_admin_income_report_request_income_report_dict = create_admin_income_report_request_income_report_instance.to_dict()
# create an instance of CreateAdminIncomeReportRequestIncomeReport from a dict
create_admin_income_report_request_income_report_from_dict = CreateAdminIncomeReportRequestIncomeReport.from_dict(create_admin_income_report_request_income_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


