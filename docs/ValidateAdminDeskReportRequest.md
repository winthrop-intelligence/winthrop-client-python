# ValidateAdminDeskReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body_html** | **str** |  | 

## Example

```python
from winthrop_client_python.models.validate_admin_desk_report_request import ValidateAdminDeskReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateAdminDeskReportRequest from a JSON string
validate_admin_desk_report_request_instance = ValidateAdminDeskReportRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateAdminDeskReportRequest.to_json())

# convert the object into a dict
validate_admin_desk_report_request_dict = validate_admin_desk_report_request_instance.to_dict()
# create an instance of ValidateAdminDeskReportRequest from a dict
validate_admin_desk_report_request_from_dict = ValidateAdminDeskReportRequest.from_dict(validate_admin_desk_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


