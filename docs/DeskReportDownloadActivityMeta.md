# DeskReportDownloadActivityMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**status** | **str** |  | 
**current_page** | **int** |  | 
**per_page** | **int** |  | 
**total_pages** | **int** |  | 
**total_entries** | **int** |  | 
**returned_entries** | **int** |  | 
**next_page** | **int** |  | 
**previous_page** | **int** |  | 
**display_timezone** | **str** |  | 
**refreshed_at** | **datetime** |  | 
**period** | [**DeskActivityMetaPeriod**](DeskActivityMetaPeriod.md) |  | 
**source** | [**DeskActivityMetaSource**](DeskActivityMetaSource.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_report_download_activity_meta import DeskReportDownloadActivityMeta

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportDownloadActivityMeta from a JSON string
desk_report_download_activity_meta_instance = DeskReportDownloadActivityMeta.from_json(json)
# print the JSON string representation of the object
print(DeskReportDownloadActivityMeta.to_json())

# convert the object into a dict
desk_report_download_activity_meta_dict = desk_report_download_activity_meta_instance.to_dict()
# create an instance of DeskReportDownloadActivityMeta from a dict
desk_report_download_activity_meta_from_dict = DeskReportDownloadActivityMeta.from_dict(desk_report_download_activity_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


