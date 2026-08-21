# DeskReportSummary

A gallery card (frontend DeskReportSummary)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**title** | **str** |  | 
**category** | **str** |  | 
**report_type** | **str** |  | 
**summary** | **str** |  | 
**headline_stats** | [**List[DeskHeadlineStat]**](DeskHeadlineStat.md) |  | 
**cover** | [**DeskReportSummaryCover**](DeskReportSummaryCover.md) |  | 
**published_at** | **datetime** |  | 
**updated_at** | **datetime** | The current version&#39;s publish time once past v1 (the UPDATED badge); null at v1 | 
**page_count** | **int** |  | 
**artifact_kinds** | **List[str]** |  | 
**artifacts** | [**List[DeskReportArtifact]**](DeskReportArtifact.md) |  | 
**rerun_cadence** | **str** |  | 
**push_example** | **str** |  | 
**unread** | **bool** | No read row for the caller, or a newer version than the one last opened | 
**request_context** | [**DeskRequestContext**](DeskRequestContext.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_report_summary import DeskReportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportSummary from a JSON string
desk_report_summary_instance = DeskReportSummary.from_json(json)
# print the JSON string representation of the object
print(DeskReportSummary.to_json())

# convert the object into a dict
desk_report_summary_dict = desk_report_summary_instance.to_dict()
# create an instance of DeskReportSummary from a dict
desk_report_summary_from_dict = DeskReportSummary.from_dict(desk_report_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


