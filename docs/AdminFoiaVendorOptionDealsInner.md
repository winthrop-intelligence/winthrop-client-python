# AdminFoiaVendorOptionDealsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor** | **str** |  | [optional] 
**start_at** | **date** |  | [optional] 
**end_at** | **date** |  | [optional] 
**autorenew** | **bool** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_foia_vendor_option_deals_inner import AdminFoiaVendorOptionDealsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaVendorOptionDealsInner from a JSON string
admin_foia_vendor_option_deals_inner_instance = AdminFoiaVendorOptionDealsInner.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaVendorOptionDealsInner.to_json())

# convert the object into a dict
admin_foia_vendor_option_deals_inner_dict = admin_foia_vendor_option_deals_inner_instance.to_dict()
# create an instance of AdminFoiaVendorOptionDealsInner from a dict
admin_foia_vendor_option_deals_inner_from_dict = AdminFoiaVendorOptionDealsInner.from_dict(admin_foia_vendor_option_deals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


