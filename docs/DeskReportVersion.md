# DeskReportVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | 
**published_at** | **datetime** |  | 
**change_note** | **str** | What changed for the reader; null on v1 | 

## Example

```python
from winthrop_client_python.models.desk_report_version import DeskReportVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DeskReportVersion from a JSON string
desk_report_version_instance = DeskReportVersion.from_json(json)
# print the JSON string representation of the object
print(DeskReportVersion.to_json())

# convert the object into a dict
desk_report_version_dict = desk_report_version_instance.to_dict()
# create an instance of DeskReportVersion from a dict
desk_report_version_from_dict = DeskReportVersion.from_dict(desk_report_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


