# Vendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deal_type_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.vendor import Vendor

# TODO update the JSON string below
json = "{}"
# create an instance of Vendor from a JSON string
vendor_instance = Vendor.from_json(json)
# print the JSON string representation of the object
print(Vendor.to_json())

# convert the object into a dict
vendor_dict = vendor_instance.to_dict()
# create an instance of Vendor from a dict
vendor_from_dict = Vendor.from_dict(vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


