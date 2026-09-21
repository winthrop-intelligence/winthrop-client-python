# DeskAdminReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskAdminReport**](DeskAdminReport.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_report_response import DeskAdminReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReportResponse from a JSON string
desk_admin_report_response_instance = DeskAdminReportResponse.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReportResponse.to_json())

# convert the object into a dict
desk_admin_report_response_dict = desk_admin_report_response_instance.to_dict()
# create an instance of DeskAdminReportResponse from a dict
desk_admin_report_response_from_dict = DeskAdminReportResponse.from_dict(desk_admin_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


