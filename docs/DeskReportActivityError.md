# DeskReportActivityError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_report_activity_error import DeskReportActivityError

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportActivityError from a JSON string
desk_report_activity_error_instance = DeskReportActivityError.from_json(json)
# print the JSON string representation of the object
print(DeskReportActivityError.to_json())

# convert the object into a dict
desk_report_activity_error_dict = desk_report_activity_error_instance.to_dict()
# create an instance of DeskReportActivityError from a dict
desk_report_activity_error_from_dict = DeskReportActivityError.from_dict(desk_report_activity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


