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
**cover_numeral** | **str** | Decorative corner mark (\&quot;24\&quot;, \&quot;AD\&quot;); blank clears it | [optional] 
**page_count** | **int** |  | [optional] 
**push_example** | **str** |  | [optional] 
**rerun_cadence** | **str** |  | [optional] 
**draft_body_html** | **str** |  | [optional] 
**account_id** | **int** | Re-scope the report (WINAD-10415 / D-29). Omit to leave the audience alone; send null to publish to every school, or an account id to move it to that school. An unauthored cover kicker follows the new audience. Refused (422) when the report answers an ask on a different account, or when a hidden report&#39;s replacement would be left outside the new audience.  | [optional] 

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


