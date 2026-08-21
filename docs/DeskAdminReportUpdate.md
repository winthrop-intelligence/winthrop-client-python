# DeskAdminReportUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**headline_stats** | [**List[DeskHeadlineStat]**](DeskHeadlineStat.md) |  | [optional] 
**cover_treatment** | **str** |  | [optional] 
**cover_kicker** | **str** | Defaults to \&quot;THE DESK · PREPARED FOR &lt;ACCOUNT&gt;\&quot; on create | [optional] 
**cover_numeral** | **str** |  | [optional] 
**page_count** | **int** |  | [optional] 
**push_example** | **str** |  | [optional] 
**rerun_cadence** | **str** |  | [optional] 
**draft_body_html** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.desk_admin_report_update import DeskAdminReportUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReportUpdate from a JSON string
desk_admin_report_update_instance = DeskAdminReportUpdate.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReportUpdate.to_json())

# convert the object into a dict
desk_admin_report_update_dict = desk_admin_report_update_instance.to_dict()
# create an instance of DeskAdminReportUpdate from a dict
desk_admin_report_update_from_dict = DeskAdminReportUpdate.from_dict(desk_admin_report_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


