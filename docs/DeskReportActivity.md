# DeskReportActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**DeskReportActivityMeta**](DeskReportActivityMeta.md) |  | 
**data** | [**List[DeskActivityViewer]**](DeskActivityViewer.md) |  | 
**summary** | [**DeskActivitySummary**](DeskActivitySummary.md) |  | 
**period_totals** | [**DeskActivitySummary**](DeskActivitySummary.md) |  | 
**error** | [**DeskReportActivityError**](DeskReportActivityError.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_report_activity import DeskReportActivity

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportActivity from a JSON string
desk_report_activity_instance = DeskReportActivity.from_json(json)
# print the JSON string representation of the object
print(DeskReportActivity.to_json())

# convert the object into a dict
desk_report_activity_dict = desk_report_activity_instance.to_dict()
# create an instance of DeskReportActivity from a dict
desk_report_activity_from_dict = DeskReportActivity.from_dict(desk_report_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


