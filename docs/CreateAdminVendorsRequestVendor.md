# CreateAdminVendorsRequestVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**deal_type_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.create_admin_vendors_request_vendor import CreateAdminVendorsRequestVendor

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminVendorsRequestVendor from a JSON string
create_admin_vendors_request_vendor_instance = CreateAdminVendorsRequestVendor.from_json(json)
# print the JSON string representation of the object
print(CreateAdminVendorsRequestVendor.to_json())

# convert the object into a dict
create_admin_vendors_request_vendor_dict = create_admin_vendors_request_vendor_instance.to_dict()
# create an instance of CreateAdminVendorsRequestVendor from a dict
create_admin_vendors_request_vendor_from_dict = CreateAdminVendorsRequestVendor.from_dict(create_admin_vendors_request_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


