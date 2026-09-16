# DeskReportOpenedResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**first_open** | **bool** |  | 
**open_count** | **int** |  | 

## Example

```python
from winthrop_client_python.models.desk_report_opened_response_data import DeskReportOpenedResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportOpenedResponseData from a JSON string
desk_report_opened_response_data_instance = DeskReportOpenedResponseData.from_json(json)
# print the JSON string representation of the object
print(DeskReportOpenedResponseData.to_json())

# convert the object into a dict
desk_report_opened_response_data_dict = desk_report_opened_response_data_instance.to_dict()
# create an instance of DeskReportOpenedResponseData from a dict
desk_report_opened_response_data_from_dict = DeskReportOpenedResponseData.from_dict(desk_report_opened_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


