# DealDetailVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_detail_vendor import DealDetailVendor

# TODO update the JSON string below
json = "{}"
# create an instance of DealDetailVendor from a JSON string
deal_detail_vendor_instance = DealDetailVendor.from_json(json)
# print the JSON string representation of the object
print(DealDetailVendor.to_json())

# convert the object into a dict
deal_detail_vendor_dict = deal_detail_vendor_instance.to_dict()
# create an instance of DealDetailVendor from a dict
deal_detail_vendor_from_dict = DealDetailVendor.from_dict(deal_detail_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


