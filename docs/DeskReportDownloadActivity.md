# DeskReportDownloadActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**DeskReportDownloadActivityMeta**](DeskReportDownloadActivityMeta.md) |  | 
**data** | [**List[DeskActivityDownload]**](DeskActivityDownload.md) |  | 
**summary** | [**DeskActivityDownloadSummary**](DeskActivityDownloadSummary.md) |  | 
**period_totals** | [**DeskActivityDownloadSummary**](DeskActivityDownloadSummary.md) |  | 
**error** | [**DeskReportActivityError**](DeskReportActivityError.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_report_download_activity import DeskReportDownloadActivity

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportDownloadActivity from a JSON string
desk_report_download_activity_instance = DeskReportDownloadActivity.from_json(json)
# print the JSON string representation of the object
print(DeskReportDownloadActivity.to_json())

# convert the object into a dict
desk_report_download_activity_dict = desk_report_download_activity_instance.to_dict()
# create an instance of DeskReportDownloadActivity from a dict
desk_report_download_activity_from_dict = DeskReportDownloadActivity.from_dict(desk_report_download_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


