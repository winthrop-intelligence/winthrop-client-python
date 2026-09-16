# DeskReportArchiveResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**archived** | **bool** |  | 

## Example

```python
from winthrop_client_python.models.desk_report_archive_response_data import DeskReportArchiveResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportArchiveResponseData from a JSON string
desk_report_archive_response_data_instance = DeskReportArchiveResponseData.from_json(json)
# print the JSON string representation of the object
print(DeskReportArchiveResponseData.to_json())

# convert the object into a dict
desk_report_archive_response_data_dict = desk_report_archive_response_data_instance.to_dict()
# create an instance of DeskReportArchiveResponseData from a dict
desk_report_archive_response_data_from_dict = DeskReportArchiveResponseData.from_dict(desk_report_archive_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


