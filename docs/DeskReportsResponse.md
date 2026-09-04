# DeskReportsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**DeskReportsResponseMeta**](DeskReportsResponseMeta.md) |  | 
**data** | [**List[DeskReportSummary]**](DeskReportSummary.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_reports_response import DeskReportsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportsResponse from a JSON string
desk_reports_response_instance = DeskReportsResponse.from_json(json)
# print the JSON string representation of the object
print(DeskReportsResponse.to_json())

# convert the object into a dict
desk_reports_response_dict = desk_reports_response_instance.to_dict()
# create an instance of DeskReportsResponse from a dict
desk_reports_response_from_dict = DeskReportsResponse.from_dict(desk_reports_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


