# AthleticProfileShowDealsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**deal_type** | **str** |  | [optional] 
**term** | **str** |  | [optional] 
**vendor_names** | **str** |  | [optional] 
**vendors** | [**List[AthleticProfileShowDealsInnerVendorsInner]**](AthleticProfileShowDealsInnerVendorsInner.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**has_contract** | **bool** |  | [optional] 
**raw_contract_id** | **int** |  | [optional] 

## Example

```python
from winthrop_client_python.models.athletic_profile_show_deals_inner import AthleticProfileShowDealsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AthleticProfileShowDealsInner from a JSON string
athletic_profile_show_deals_inner_instance = AthleticProfileShowDealsInner.from_json(json)
# print the JSON string representation of the object
print(AthleticProfileShowDealsInner.to_json())

# convert the object into a dict
athletic_profile_show_deals_inner_dict = athletic_profile_show_deals_inner_instance.to_dict()
# create an instance of AthleticProfileShowDealsInner from a dict
athletic_profile_show_deals_inner_from_dict = AthleticProfileShowDealsInner.from_dict(athletic_profile_show_deals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


