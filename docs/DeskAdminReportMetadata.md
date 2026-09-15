# DeskAdminReportMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**report_type** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**cover_treatment** | **str** |  | [optional] 
**cover_kicker** | **str** | Defaults to \&quot;THE DESK · PREPARED FOR &lt;ACCOUNT&gt;\&quot; on create | [optional] 
**cover_numeral** | **str** | Decorative corner mark (\&quot;24\&quot;, \&quot;AD\&quot;); blank clears it | [optional] 
**page_count** | **int** |  | [optional] 
**push_example** | **str** |  | [optional] 
**rerun_cadence** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.desk_admin_report_metadata import DeskAdminReportMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReportMetadata from a JSON string
desk_admin_report_metadata_instance = DeskAdminReportMetadata.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReportMetadata.to_json())

# convert the object into a dict
desk_admin_report_metadata_dict = desk_admin_report_metadata_instance.to_dict()
# create an instance of DeskAdminReportMetadata from a dict
desk_admin_report_metadata_from_dict = DeskAdminReportMetadata.from_dict(desk_admin_report_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


