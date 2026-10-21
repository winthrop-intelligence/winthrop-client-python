# AdminFoiaVendorOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | FOIA-requestable deal type ID. | 
**name** | **str** |  | 
**status** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 
**requested_item_id** | **int** |  | [optional] 
**deals** | [**List[AdminFoiaVendorOptionDealsInner]**](AdminFoiaVendorOptionDealsInner.md) |  | 

## Example

```python
from winthrop_client_python.models.admin_foia_vendor_option import AdminFoiaVendorOption

# TODO update the JSON string below
json = "{}"
# create an instance of AdminFoiaVendorOption from a JSON string
admin_foia_vendor_option_instance = AdminFoiaVendorOption.from_json(json)
# print the JSON string representation of the object
print(AdminFoiaVendorOption.to_json())

# convert the object into a dict
admin_foia_vendor_option_dict = admin_foia_vendor_option_instance.to_dict()
# create an instance of AdminFoiaVendorOption from a dict
admin_foia_vendor_option_from_dict = AdminFoiaVendorOption.from_dict(admin_foia_vendor_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


