# DeskAdminPublishResponseDataReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**title** | **str** |  | 
**published_at** | **datetime** |  | 
**version_number** | **int** |  | 
**artifact_kinds** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_publish_response_data_report import DeskAdminPublishResponseDataReport

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminPublishResponseDataReport from a JSON string
desk_admin_publish_response_data_report_instance = DeskAdminPublishResponseDataReport.from_json(json)
# print the JSON string representation of the object
print(DeskAdminPublishResponseDataReport.to_json())

# convert the object into a dict
desk_admin_publish_response_data_report_dict = desk_admin_publish_response_data_report_instance.to_dict()
# create an instance of DeskAdminPublishResponseDataReport from a dict
desk_admin_publish_response_data_report_from_dict = DeskAdminPublishResponseDataReport.from_dict(desk_admin_publish_response_data_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


