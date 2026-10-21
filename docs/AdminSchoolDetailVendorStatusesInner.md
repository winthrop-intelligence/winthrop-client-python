# AdminSchoolDetailVendorStatusesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 
**deal_type_name** | **str** |  | [optional] 
**deal_status_type_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_school_detail_vendor_statuses_inner import AdminSchoolDetailVendorStatusesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminSchoolDetailVendorStatusesInner from a JSON string
admin_school_detail_vendor_statuses_inner_instance = AdminSchoolDetailVendorStatusesInner.from_json(json)
# print the JSON string representation of the object
print(AdminSchoolDetailVendorStatusesInner.to_json())

# convert the object into a dict
admin_school_detail_vendor_statuses_inner_dict = admin_school_detail_vendor_statuses_inner_instance.to_dict()
# create an instance of AdminSchoolDetailVendorStatusesInner from a dict
admin_school_detail_vendor_statuses_inner_from_dict = AdminSchoolDetailVendorStatusesInner.from_dict(admin_school_detail_vendor_statuses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


