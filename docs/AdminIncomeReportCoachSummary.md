# AdminIncomeReportCoachSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**income_report_text** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_income_report_coach_summary import AdminIncomeReportCoachSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminIncomeReportCoachSummary from a JSON string
admin_income_report_coach_summary_instance = AdminIncomeReportCoachSummary.from_json(json)
# print the JSON string representation of the object
print(AdminIncomeReportCoachSummary.to_json())

# convert the object into a dict
admin_income_report_coach_summary_dict = admin_income_report_coach_summary_instance.to_dict()
# create an instance of AdminIncomeReportCoachSummary from a dict
admin_income_report_coach_summary_from_dict = AdminIncomeReportCoachSummary.from_dict(admin_income_report_coach_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


