# AdminVendorsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deal_types** | [**List[ContactSearchCoachOptionsSportsInner]**](ContactSearchCoachOptionsSportsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_vendors_options import AdminVendorsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendorsOptions from a JSON string
admin_vendors_options_instance = AdminVendorsOptions.from_json(json)
# print the JSON string representation of the object
print(AdminVendorsOptions.to_json())

# convert the object into a dict
admin_vendors_options_dict = admin_vendors_options_instance.to_dict()
# create an instance of AdminVendorsOptions from a dict
admin_vendors_options_from_dict = AdminVendorsOptions.from_dict(admin_vendors_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


