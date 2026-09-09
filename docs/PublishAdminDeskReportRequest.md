# PublishAdminDeskReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_html** | **str** |  | [optional] 
**note** | **str** | The version&#39;s 06.5 history line (internal) | [optional] 
**change_note** | **str** | What changed for the reader (D-23). Required when the report already has a live version — an update without one is refused (422, nothing stored).  | [optional] 
**renotify** | **bool** | 06.5&#39;s re-notify box — re-send the delivery email for a new version | [optional] 

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


