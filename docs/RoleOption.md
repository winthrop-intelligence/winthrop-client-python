# RoleOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**section** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.role_option import RoleOption

# TODO update the JSON string below
json = "{}"
# create an instance of RoleOption from a JSON string
role_option_instance = RoleOption.from_json(json)
# print the JSON string representation of the object
print(RoleOption.to_json())

# convert the object into a dict
role_option_dict = role_option_instance.to_dict()
# create an instance of RoleOption from a dict
role_option_from_dict = RoleOption.from_dict(role_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


