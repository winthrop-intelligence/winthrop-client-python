# AdminImpersonation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impersonated_user** | [**AdminImpersonationImpersonatedUser**](AdminImpersonationImpersonatedUser.md) |  | [optional] 
**admin_user_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_impersonation import AdminImpersonation

# TODO update the JSON string below
json = "{}"
# create an instance of AdminImpersonation from a JSON string
admin_impersonation_instance = AdminImpersonation.from_json(json)
# print the JSON string representation of the object
print(AdminImpersonation.to_json())

# convert the object into a dict
admin_impersonation_dict = admin_impersonation_instance.to_dict()
# create an instance of AdminImpersonation from a dict
admin_impersonation_from_dict = AdminImpersonation.from_dict(admin_impersonation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


