# AdminVendorValidationErrorConflictingVendor

Present only when the name is equivalent to another vendor's.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from winthrop_client_python.models.admin_vendor_validation_error_conflicting_vendor import AdminVendorValidationErrorConflictingVendor

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendorValidationErrorConflictingVendor from a JSON string
admin_vendor_validation_error_conflicting_vendor_instance = AdminVendorValidationErrorConflictingVendor.from_json(json)
# print the JSON string representation of the object
print(AdminVendorValidationErrorConflictingVendor.to_json())

# convert the object into a dict
admin_vendor_validation_error_conflicting_vendor_dict = admin_vendor_validation_error_conflicting_vendor_instance.to_dict()
# create an instance of AdminVendorValidationErrorConflictingVendor from a dict
admin_vendor_validation_error_conflicting_vendor_from_dict = AdminVendorValidationErrorConflictingVendor.from_dict(admin_vendor_validation_error_conflicting_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


