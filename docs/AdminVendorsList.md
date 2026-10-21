# AdminVendorsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | [optional] 
**data** | [**List[AdminVendor]**](AdminVendor.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_vendors_list import AdminVendorsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendorsList from a JSON string
admin_vendors_list_instance = AdminVendorsList.from_json(json)
# print the JSON string representation of the object
print(AdminVendorsList.to_json())

# convert the object into a dict
admin_vendors_list_dict = admin_vendors_list_instance.to_dict()
# create an instance of AdminVendorsList from a dict
admin_vendors_list_from_dict = AdminVendorsList.from_dict(admin_vendors_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


