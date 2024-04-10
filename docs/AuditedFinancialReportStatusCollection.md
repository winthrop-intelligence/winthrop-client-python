# AuditedFinancialReportStatusCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuditedFinancialReportStatus]**](AuditedFinancialReportStatus.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.audited_financial_report_status_collection import AuditedFinancialReportStatusCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AuditedFinancialReportStatusCollection from a JSON string
audited_financial_report_status_collection_instance = AuditedFinancialReportStatusCollection.from_json(json)
# print the JSON string representation of the object
print(AuditedFinancialReportStatusCollection.to_json())

# convert the object into a dict
audited_financial_report_status_collection_dict = audited_financial_report_status_collection_instance.to_dict()
# create an instance of AuditedFinancialReportStatusCollection from a dict
audited_financial_report_status_collection_form_dict = audited_financial_report_status_collection.from_dict(audited_financial_report_status_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


