# DeskAdminReportCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**category** | **str** |  | 
**report_type** | **str** |  | 
**summary** | **str** |  | [optional] 
**headline_stats** | [**List[DeskHeadlineStat]**](DeskHeadlineStat.md) |  | [optional] 
**cover_treatment** | **str** |  | [optional] 
**cover_kicker** | **str** | Defaults to \&quot;THE DESK · PREPARED FOR &lt;ACCOUNT&gt;\&quot; on create | [optional] 
**cover_numeral** | **str** | Decorative corner mark (\&quot;24\&quot;, \&quot;AD\&quot;); blank clears it | [optional] 
**page_count** | **int** |  | [optional] 
**push_example** | **str** |  | [optional] 
**rerun_cadence** | **str** |  | [optional] 
**account_id** | **int** |  | 
**desk_request_uuid** | **str** | The queue ask this report answers (same account) | [optional] 
**draft_body_html** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.desk_admin_report_create import DeskAdminReportCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReportCreate from a JSON string
desk_admin_report_create_instance = DeskAdminReportCreate.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReportCreate.to_json())

# convert the object into a dict
desk_admin_report_create_dict = desk_admin_report_create_instance.to_dict()
# create an instance of DeskAdminReportCreate from a dict
desk_admin_report_create_from_dict = DeskAdminReportCreate.from_dict(desk_admin_report_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


