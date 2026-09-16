# HideAdminDeskReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | 
**redirect_to_uuid** | **str** |  | [optional] 
**point_old_links** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.hide_admin_desk_report_request import HideAdminDeskReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HideAdminDeskReportRequest from a JSON string
hide_admin_desk_report_request_instance = HideAdminDeskReportRequest.from_json(json)
# print the JSON string representation of the object
print(HideAdminDeskReportRequest.to_json())

# convert the object into a dict
hide_admin_desk_report_request_dict = hide_admin_desk_report_request_instance.to_dict()
# create an instance of HideAdminDeskReportRequest from a dict
hide_admin_desk_report_request_from_dict = HideAdminDeskReportRequest.from_dict(hide_admin_desk_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


