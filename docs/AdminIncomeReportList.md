# AdminIncomeReportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminIncomeReportListMeta**](AdminIncomeReportListMeta.md) |  | [optional] 
**data** | [**List[AdminIncomeReport]**](AdminIncomeReport.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_income_report_list import AdminIncomeReportList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminIncomeReportList from a JSON string
admin_income_report_list_instance = AdminIncomeReportList.from_json(json)
# print the JSON string representation of the object
print(AdminIncomeReportList.to_json())

# convert the object into a dict
admin_income_report_list_dict = admin_income_report_list_instance.to_dict()
# create an instance of AdminIncomeReportList from a dict
admin_income_report_list_from_dict = AdminIncomeReportList.from_dict(admin_income_report_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


