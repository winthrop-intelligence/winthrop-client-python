# UpdateAdminVendorsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | [**UpdateAdminVendorsRequestVendor**](UpdateAdminVendorsRequestVendor.md) |  | 

## Example

```python
from winthrop_client_python.models.update_admin_vendors_request import UpdateAdminVendorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminVendorsRequest from a JSON string
update_admin_vendors_request_instance = UpdateAdminVendorsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminVendorsRequest.to_json())

# convert the object into a dict
update_admin_vendors_request_dict = update_admin_vendors_request_instance.to_dict()
# create an instance of UpdateAdminVendorsRequest from a dict
update_admin_vendors_request_from_dict = UpdateAdminVendorsRequest.from_dict(update_admin_vendors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


