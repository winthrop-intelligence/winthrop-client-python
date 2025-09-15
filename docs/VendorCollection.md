# VendorCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Vendor]**](Vendor.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.vendor_collection import VendorCollection

# TODO update the JSON string below
json = "{}"
# create an instance of VendorCollection from a JSON string
vendor_collection_instance = VendorCollection.from_json(json)
# print the JSON string representation of the object
print(VendorCollection.to_json())

# convert the object into a dict
vendor_collection_dict = vendor_collection_instance.to_dict()
# create an instance of VendorCollection from a dict
vendor_collection_form_dict = vendor_collection.from_dict(vendor_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


