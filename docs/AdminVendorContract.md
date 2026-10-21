# AdminVendorContract


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**school_id** | **int** |  | [optional] 
**school_name** | **str** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**deal_type_name** | **str** |  | [optional] 
**vendors** | [**List[ContactSearchCoachOptionsCoachesInner]**](ContactSearchCoachOptionsCoachesInner.md) |  | [optional] 
**start_at** | **datetime** |  | [optional] 
**end_at** | **datetime** |  | [optional] 
**verified** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_vendor_contract import AdminVendorContract

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendorContract from a JSON string
admin_vendor_contract_instance = AdminVendorContract.from_json(json)
# print the JSON string representation of the object
print(AdminVendorContract.to_json())

# convert the object into a dict
admin_vendor_contract_dict = admin_vendor_contract_instance.to_dict()
# create an instance of AdminVendorContract from a dict
admin_vendor_contract_from_dict = AdminVendorContract.from_dict(admin_vendor_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


