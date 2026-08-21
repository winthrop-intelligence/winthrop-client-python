# DeskAdminVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | 
**note** | **str** |  | 
**published_at** | **datetime** |  | 
**published_by** | **str** |  | 

## Example

```python
from winthrop_client_python.models.desk_admin_version import DeskAdminVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DeskAdminVersion from a JSON string
desk_admin_version_instance = DeskAdminVersion.from_json(json)
# print the JSON string representation of the object
print(DeskAdminVersion.to_json())

# convert the object into a dict
desk_admin_version_dict = desk_admin_version_instance.to_dict()
# create an instance of DeskAdminVersion from a dict
desk_admin_version_from_dict = DeskAdminVersion.from_dict(desk_admin_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


