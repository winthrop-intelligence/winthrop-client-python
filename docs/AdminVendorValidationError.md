# AdminVendorValidationError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **Dict[str, List[str]]** |  | 
**conflicting_vendor** | [**AdminVendorValidationErrorConflictingVendor**](AdminVendorValidationErrorConflictingVendor.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_vendor_validation_error import AdminVendorValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AdminVendorValidationError from a JSON string
admin_vendor_validation_error_instance = AdminVendorValidationError.from_json(json)
# print the JSON string representation of the object
print(AdminVendorValidationError.to_json())

# convert the object into a dict
admin_vendor_validation_error_dict = admin_vendor_validation_error_instance.to_dict()
# create an instance of AdminVendorValidationError from a dict
admin_vendor_validation_error_from_dict = AdminVendorValidationError.from_dict(admin_vendor_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


