# PublishAdminDeskReportRequest

First publication sends body_html and optional note/change_note/renotify fields. Publishing a new version requires update, a JSON-encoded DeskAdminReportPublishUpdate; top-level publication fields are ignored when update is present. File uploads require multipart/form-data and travel in downloads[pdf], downloads[xlsx] and downloads[pptx]. An update without new files may also send the JSON-encoded update field as application/json. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_html** | **str** |  | [optional] 
**note** | **str** | The version&#39;s 06.5 history line (internal) | [optional] 
**change_note** | **str** | Reader-facing explanation; new versions send this inside update instead. | [optional] 
**renotify** | **bool** | Request notification; effective only when publish notifications are enabled. | [optional] 
**update** | **str** | JSON-encoded DeskAdminReportPublishUpdate. Required for a new version, omitted for first publication. Only edited fields need to be sent.  | [optional] 
**downloads_pdf** | **bytearray** | PDF replacement or addition; multipart updates only. | [optional] 
**downloads_xlsx** | **bytearray** | XLSX replacement or addition; multipart updates only. | [optional] 
**downloads_pptx** | **bytearray** | PPTX replacement or addition; multipart updates only. | [optional] 

## Example

```python
from winthrop_client_python.models.publish_admin_desk_report_request import PublishAdminDeskReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishAdminDeskReportRequest from a JSON string
publish_admin_desk_report_request_instance = PublishAdminDeskReportRequest.from_json(json)
# print the JSON string representation of the object
print(PublishAdminDeskReportRequest.to_json())

# convert the object into a dict
publish_admin_desk_report_request_dict = publish_admin_desk_report_request_instance.to_dict()
# create an instance of PublishAdminDeskReportRequest from a dict
publish_admin_desk_report_request_from_dict = PublishAdminDeskReportRequest.from_dict(publish_admin_desk_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


