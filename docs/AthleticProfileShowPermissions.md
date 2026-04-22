# AthleticProfileShowPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_see_personnel** | **bool** |  | [optional] 
**can_see_compensation** | **bool** |  | [optional] 
**can_see_financials** | **bool** |  | [optional] 
**can_see_deals** | **bool** |  | [optional] 
**can_see_guarantees** | **bool** |  | [optional] 
**can_show_schedule** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_permissions import AthleticProfileShowPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowPermissions from a JSON string
athletic_profile_show_permissions_instance = AthleticProfileShowPermissions.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowPermissions.to_json())

# convert the object into a dict
athletic_profile_show_permissions_dict = athletic_profile_show_permissions_instance.to_dict()
# create an instance of AthleticProfileShowPermissions from a dict
athletic_profile_show_permissions_from_dict = AthleticProfileShowPermissions.from_dict(athletic_profile_show_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


