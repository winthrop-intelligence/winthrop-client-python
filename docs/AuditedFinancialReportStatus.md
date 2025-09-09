# AuditedFinancialReportStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | 
**year** | **int** |  | 
**status** | **str** | The status of the audited financial report. Available means the report is in the system. Missing means the report is not in the system. Not Available means the report is not required for the year. | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from winthrop_client_python.models.audited_financial_report_status import AuditedFinancialReportStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AuditedFinancialReportStatus from a JSON string
audited_financial_report_status_instance = AuditedFinancialReportStatus.from_json(json)
# print the JSON string representation of the object
print(AuditedFinancialReportStatus.to_json())

# convert the object into a dict
audited_financial_report_status_dict = audited_financial_report_status_instance.to_dict()
# create an instance of AuditedFinancialReportStatus from a dict
audited_financial_report_status_from_dict = AuditedFinancialReportStatus.from_dict(audited_financial_report_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


