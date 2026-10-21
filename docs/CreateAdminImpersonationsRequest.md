# CreateAdminImpersonationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | id of the user to impersonate | 

## Example

```python
from winthrop_client_python.models.create_admin_impersonations_request import CreateAdminImpersonationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminImpersonationsRequest from a JSON string
create_admin_impersonations_request_instance = CreateAdminImpersonationsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminImpersonationsRequest.to_json())

# convert the object into a dict
create_admin_impersonations_request_dict = create_admin_impersonations_request_instance.to_dict()
# create an instance of CreateAdminImpersonationsRequest from a dict
create_admin_impersonations_request_from_dict = CreateAdminImpersonationsRequest.from_dict(create_admin_impersonations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


