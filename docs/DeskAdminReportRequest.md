# DeskAdminReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**status** | **str** |  | 
**requester_name** | **str** |  | 
**body** | **str** |  | 
**category** | **str** | The customer&#39;s 03.1 tile choice; null when none was picked | 
**cta_key** | **str** | The reader CTA the ask started from; null for a guided ask | 
**source_report_title** | **str** | The title of the report that CTA was read on; null with cta_key | 
**received_at** | **datetime** |  | 
**clock_paused** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_report_request import DeskAdminReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReportRequest from a JSON string
desk_admin_report_request_instance = DeskAdminReportRequest.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReportRequest.to_json())

# convert the object into a dict
desk_admin_report_request_dict = desk_admin_report_request_instance.to_dict()
# create an instance of DeskAdminReportRequest from a dict
desk_admin_report_request_from_dict = DeskAdminReportRequest.from_dict(desk_admin_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


