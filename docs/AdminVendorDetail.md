# AdminVendorDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**deal_type_id** | **int** |  | [optional] 
**deals_count** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deal_type** | [**AdminCoachCurrentSport**](AdminCoachCurrentSport.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_vendor_detail import AdminVendorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendorDetail from a JSON string
admin_vendor_detail_instance = AdminVendorDetail.from_json(json)
# print the JSON string representation of the object
print(AdminVendorDetail.to_json())

# convert the object into a dict
admin_vendor_detail_dict = admin_vendor_detail_instance.to_dict()
# create an instance of AdminVendorDetail from a dict
admin_vendor_detail_from_dict = AdminVendorDetail.from_dict(admin_vendor_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


