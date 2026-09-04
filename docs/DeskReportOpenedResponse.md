# DeskReportOpenedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeskReportOpenedResponseData**](DeskReportOpenedResponseData.md) |  | 

## Example

```python
from winthrop_client_python.models.desk_report_opened_response import DeskReportOpenedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportOpenedResponse from a JSON string
desk_report_opened_response_instance = DeskReportOpenedResponse.from_json(json)
# print the JSON string representation of the object
print(DeskReportOpenedResponse.to_json())

# convert the object into a dict
desk_report_opened_response_dict = desk_report_opened_response_instance.to_dict()
# create an instance of DeskReportOpenedResponse from a dict
desk_report_opened_response_from_dict = DeskReportOpenedResponse.from_dict(desk_report_opened_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


