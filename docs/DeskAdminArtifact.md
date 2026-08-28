# DeskAdminArtifact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**kind** | **str** |  | 
**filename** | **str** |  | 
**byte_size** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_artifact import DeskAdminArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminArtifact from a JSON string
desk_admin_artifact_instance = DeskAdminArtifact.from_json(json)
# print the JSON string representation of the object
print(DeskAdminArtifact.to_json())

# convert the object into a dict
desk_admin_artifact_dict = desk_admin_artifact_instance.to_dict()
# create an instance of DeskAdminArtifact from a dict
desk_admin_artifact_from_dict = DeskAdminArtifact.from_dict(desk_admin_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


