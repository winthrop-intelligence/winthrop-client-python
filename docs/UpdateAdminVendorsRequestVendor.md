# UpdateAdminVendorsRequestVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_admin_vendors_request_vendor import UpdateAdminVendorsRequestVendor

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminVendorsRequestVendor from a JSON string
update_admin_vendors_request_vendor_instance = UpdateAdminVendorsRequestVendor.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminVendorsRequestVendor.to_json())

# convert the object into a dict
update_admin_vendors_request_vendor_dict = update_admin_vendors_request_vendor_instance.to_dict()
# create an instance of UpdateAdminVendorsRequestVendor from a dict
update_admin_vendors_request_vendor_from_dict = UpdateAdminVendorsRequestVendor.from_dict(update_admin_vendors_request_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


