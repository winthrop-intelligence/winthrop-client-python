# DeskActivityMetaSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**environment** | **str** |  | 
**cache_seconds** | **int** |  | 
**coverage** | [**DeskActivityMetaSourceCoverage**](DeskActivityMetaSourceCoverage.md) |  | 
**limitations** | **List[str]** |  | 

## Example

```python
from winthrop_client_python.models.desk_activity_meta_source import DeskActivityMetaSource

# TODO update the JSON string below
json = "{}"
# create an instance of DeskActivityMetaSource from a JSON string
desk_activity_meta_source_instance = DeskActivityMetaSource.from_json(json)
# print the JSON string representation of the object
print(DeskActivityMetaSource.to_json())

# convert the object into a dict
desk_activity_meta_source_dict = desk_activity_meta_source_instance.to_dict()
# create an instance of DeskActivityMetaSource from a dict
desk_activity_meta_source_from_dict = DeskActivityMetaSource.from_dict(desk_activity_meta_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


