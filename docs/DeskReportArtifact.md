# DeskReportArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**filename** | **str** |  | 
**url** | **str** | ActiveStorage download URL (attachment disposition) | 

## Example

```python
from winthrop_client_python.models.desk_report_artifact import DeskReportArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportArtifact from a JSON string
desk_report_artifact_instance = DeskReportArtifact.from_json(json)
# print the JSON string representation of the object
print(DeskReportArtifact.to_json())

# convert the object into a dict
desk_report_artifact_dict = desk_report_artifact_instance.to_dict()
# create an instance of DeskReportArtifact from a dict
desk_report_artifact_from_dict = DeskReportArtifact.from_dict(desk_report_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


