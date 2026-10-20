# AdminFoiaFollowUpReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**AdminFoiaFollowUpReportMeta**](AdminFoiaFollowUpReportMeta.md) |  | [optional] 
**data** | [**List[AdminFoiaFollowUpReportDataInner]**](AdminFoiaFollowUpReportDataInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_follow_up_report import AdminFoiaFollowUpReport

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaFollowUpReport from a JSON string
admin_foia_follow_up_report_instance = AdminFoiaFollowUpReport.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaFollowUpReport.to_json())

# convert the object into a dict
admin_foia_follow_up_report_dict = admin_foia_follow_up_report_instance.to_dict()
# create an instance of AdminFoiaFollowUpReport from a dict
admin_foia_follow_up_report_from_dict = AdminFoiaFollowUpReport.from_dict(admin_foia_follow_up_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


