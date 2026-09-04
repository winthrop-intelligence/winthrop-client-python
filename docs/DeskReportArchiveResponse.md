# DeskReportArchiveResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskReportArchiveResponseData**](DeskReportArchiveResponseData.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_report_archive_response import DeskReportArchiveResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportArchiveResponse from a JSON string
desk_report_archive_response_instance = DeskReportArchiveResponse.from_json(json)
# print the JSON string representation of the object
print(DeskReportArchiveResponse.to_json())

# convert the object into a dict
desk_report_archive_response_dict = desk_report_archive_response_instance.to_dict()
# create an instance of DeskReportArchiveResponse from a dict
desk_report_archive_response_from_dict = DeskReportArchiveResponse.from_dict(desk_report_archive_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


