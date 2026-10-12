# GetAdminDeskReportActivity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**meta** | [**DeskReportDownloadActivityMeta**](DeskReportDownloadActivityMeta.md) |  | 
**data** | [**List[DeskActivityDownload]**](DeskActivityDownload.md) |  | 
**summary** | [**DeskActivityDownloadSummary**](DeskActivityDownloadSummary.md) |  | 
**period_totals** | [**DeskActivityDownloadSummary**](DeskActivityDownloadSummary.md) |  | 
**error** | [**DeskReportActivityError**](DeskReportActivityError.md) |  | 

## Example

```python
from winthrop_client_python.models.get_admin_desk_report_activity200_response import GetAdminDeskReportActivity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdminDeskReportActivity200Response from a JSON string
get_admin_desk_report_activity200_response_instance = GetAdminDeskReportActivity200Response.from_json(json)
# print the JSON string representation of the object
print(GetAdminDeskReportActivity200Response.to_json())

# convert the object into a dict
get_admin_desk_report_activity200_response_dict = get_admin_desk_report_activity200_response_instance.to_dict()
# create an instance of GetAdminDeskReportActivity200Response from a dict
get_admin_desk_report_activity200_response_from_dict = GetAdminDeskReportActivity200Response.from_dict(get_admin_desk_report_activity200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


