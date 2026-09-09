# DeskAdminReport

ReportAdmin (tmp/desk/TICKETS.md D-15) — the update screen and compose reopen payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**account** | [**DeskAdminAccount**](DeskAdminAccount.md) | The report&#39;s audience; null &#x3D; every school (WINAD-10415 / D-29) | 
**audience_user_count** | **int** | How many active users the report is visible to right now (Desk::Audience) — the update screen&#39;s every-school confirm. Detail responses only.  | [optional] 
**status** | **str** |  | 
**admin_status** | **str** | The queue vocabulary; building folds into draft | 
**hidden_reason** | **str** |  | 
**hidden_at** | **datetime** |  | 
**title** | **str** |  | 
**category** | **str** |  | 
**report_type** | **str** |  | 
**summary** | **str** |  | 
**headline_stats** | [**List[DeskHeadlineStat]**](DeskHeadlineStat.md) |  | 
**cover** | [**DeskAdminReportCover**](DeskAdminReportCover.md) |  | 
**page_count** | **int** |  | 
**push_example** | **str** |  | 
**rerun_cadence** | **str** |  | 
**published_at** | **datetime** |  | 
**updated_at** | **datetime** | The current version&#39;s publish time once past v1 | 
**body_html** | **str** | The CURRENT published body | [optional] 
**draft_body_html** | **str** | The compose draft, never published HTML | [optional] 
**has_html** | **bool** |  | 
**version_number** | **int** |  | 
**artifact_kinds** | **List[str]** |  | 
**artifacts** | [**List[DeskAdminArtifact]**](DeskAdminArtifact.md) |  | 
**versions** | [**List[DeskAdminVersion]**](DeskAdminVersion.md) | Newest first | [optional] 
**request** | [**DeskAdminReportRequest**](DeskAdminReportRequest.md) |  | 
**turnaround_label** | **str** | Ask-to-publish clock (\&quot;5h 34m\&quot;), pauses excluded | 

## Example

```python
from winthrop_client_python.models.desk_admin_report import DeskAdminReport

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReport from a JSON string
desk_admin_report_instance = DeskAdminReport.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReport.to_json())

# convert the object into a dict
desk_admin_report_dict = desk_admin_report_instance.to_dict()
# create an instance of DeskAdminReport from a dict
desk_admin_report_from_dict = DeskAdminReport.from_dict(desk_admin_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


