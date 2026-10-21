# AdminVendor


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
from winthrop_client_python.models.admin_vendor import AdminVendor

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendor from a JSON string
admin_vendor_instance = AdminVendor.from_json(json)
# print the JSON string representation of the object
print(AdminVendor.to_json())

# convert the object into a dict
admin_vendor_dict = admin_vendor_instance.to_dict()
# create an instance of AdminVendor from a dict
admin_vendor_from_dict = AdminVendor.from_dict(admin_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


