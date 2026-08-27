# DeskReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskReportFull**](DeskReportFull.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_report_response import DeskReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportResponse from a JSON string
desk_report_response_instance = DeskReportResponse.from_json(json)
# print the JSON string representation of the object
print(DeskReportResponse.to_json())

# convert the object into a dict
desk_report_response_dict = desk_report_response_instance.to_dict()
# create an instance of DeskReportResponse from a dict
desk_report_response_from_dict = DeskReportResponse.from_dict(desk_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


