# AdminImpersonationImpersonatedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_impersonation_impersonated_user import AdminImpersonationImpersonatedUser

# TODO update the JSON string below
json = "{}"
# create an instance of AdminImpersonationImpersonatedUser from a JSON string
admin_impersonation_impersonated_user_instance = AdminImpersonationImpersonatedUser.from_json(json)
# print the JSON string representation of the object
print(AdminImpersonationImpersonatedUser.to_json())

# convert the object into a dict
admin_impersonation_impersonated_user_dict = admin_impersonation_impersonated_user_instance.to_dict()
# create an instance of AdminImpersonationImpersonatedUser from a dict
admin_impersonation_impersonated_user_from_dict = AdminImpersonationImpersonatedUser.from_dict(admin_impersonation_impersonated_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


