# DeskActivityMetaSourceCoverage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasons** | **List[str]** |  | 
**available_from** | **datetime** |  | [optional] 
**retained_from** | **datetime** | Omitted when source retention is unlimited. | [optional] 
**retention_days** | **int** | Omitted when source retention is unlimited. | [optional] 
**source_events** | **int** |  | [optional] 
**unknown_events** | **int** |  | [optional] 
**legacy_file_events** | **int** |  | [optional] 
**missing_version_events** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.desk_activity_meta_source_coverage import DeskActivityMetaSourceCoverage

# TODO update the JSON string below
json = "{}"
# create an instance of DeskActivityMetaSourceCoverage from a JSON string
desk_activity_meta_source_coverage_instance = DeskActivityMetaSourceCoverage.from_json(json)
# print the JSON string representation of the object
print(DeskActivityMetaSourceCoverage.to_json())

# convert the object into a dict
desk_activity_meta_source_coverage_dict = desk_activity_meta_source_coverage_instance.to_dict()
# create an instance of DeskActivityMetaSourceCoverage from a dict
desk_activity_meta_source_coverage_from_dict = DeskActivityMetaSourceCoverage.from_dict(desk_activity_meta_source_coverage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


