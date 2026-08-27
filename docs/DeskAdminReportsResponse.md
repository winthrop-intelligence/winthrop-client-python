# DeskAdminReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**DeskAdminReportsResponseMeta**](DeskAdminReportsResponseMeta.md) |  | 
**data** | [**List[DeskAdminReport]**](DeskAdminReport.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_reports_response import DeskAdminReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminReportsResponse from a JSON string
desk_admin_reports_response_instance = DeskAdminReportsResponse.from_json(json)
# print the JSON string representation of the object
print(DeskAdminReportsResponse.to_json())

# convert the object into a dict
desk_admin_reports_response_dict = desk_admin_reports_response_instance.to_dict()
# create an instance of DeskAdminReportsResponse from a dict
desk_admin_reports_response_from_dict = DeskAdminReportsResponse.from_dict(desk_admin_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


