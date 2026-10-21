# AdminSportReportSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name_display** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_sport_report_summary import AdminSportReportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSportReportSummary from a JSON string
admin_sport_report_summary_instance = AdminSportReportSummary.from_json(json)
# print the JSON string representation of the object
print(AdminSportReportSummary.to_json())

# convert the object into a dict
admin_sport_report_summary_dict = admin_sport_report_summary_instance.to_dict()
# create an instance of AdminSportReportSummary from a dict
admin_sport_report_summary_from_dict = AdminSportReportSummary.from_dict(admin_sport_report_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


