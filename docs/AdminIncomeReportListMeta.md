# AdminIncomeReportListMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**next_page** | **int** |  | [optional] 
**previous_page** | **int** |  | [optional] 
**contract_status_options** | [**List[AdminIncomeReportContractStatusSummary]**](AdminIncomeReportContractStatusSummary.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_income_report_list_meta import AdminIncomeReportListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AdminIncomeReportListMeta from a JSON string
admin_income_report_list_meta_instance = AdminIncomeReportListMeta.from_json(json)
# print the JSON string representation of the object
print(AdminIncomeReportListMeta.to_json())

# convert the object into a dict
admin_income_report_list_meta_dict = admin_income_report_list_meta_instance.to_dict()
# create an instance of AdminIncomeReportListMeta from a dict
admin_income_report_list_meta_from_dict = AdminIncomeReportListMeta.from_dict(admin_income_report_list_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


