# DeskReportFull


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
**unread** | **bool** | No read row for the caller, or a newer version than the one last opened. Archiving (D-24) creates the row, so an archived-but-never-opened report is not unread — \&quot;unread\&quot; is the badge rule, not \&quot;never opened\&quot;; first_open on the full payload is the latter.  | 
**archived** | **bool** | The caller archived this report (per user, WINAD-10348 / D-24) | 
**request_context** | [**DeskRequestContext**](DeskRequestContext.md) |  | 
**body_html** | **str** | Sanitized desk-report v1 markup (doc/desk/report-markup.md) | 
**versions** | [**List[DeskReportVersion]**](DeskReportVersion.md) | The reader&#39;s \&quot;What changed\&quot; list (D-23): every published version, newest first, with the reader-facing change note only — the internal history note never leaves the admin API. v1 carries no note (\&quot;First edition\&quot;).  | 
**sections** | [**List[DeskReportFullAllOfSections]**](DeskReportFullAllOfSections.md) |  | 
**version_number** | **int** |  | 
**first_open** | **bool** | True when the caller has no read row yet (drives the 04.2 provenance strip) | 

## Example

```python
from winthrop_client_python.models.desk_report_full import DeskReportFull

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportFull from a JSON string
desk_report_full_instance = DeskReportFull.from_json(json)
# print the JSON string representation of the object
print(DeskReportFull.to_json())

# convert the object into a dict
desk_report_full_dict = desk_report_full_instance.to_dict()
# create an instance of DeskReportFull from a dict
desk_report_full_from_dict = DeskReportFull.from_dict(desk_report_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


