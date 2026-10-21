# AdminDealsOptionsDealTypesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**name_display** | **str** |  | [optional] 
**deal_detail_fields** | [**List[AdminDealsOptionsDealTypesInnerDealDetailFieldsInner]**](AdminDealsOptionsDealTypesInnerDealDetailFieldsInner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deals_options_deal_types_inner import AdminDealsOptionsDealTypesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealsOptionsDealTypesInner from a JSON string
admin_deals_options_deal_types_inner_instance = AdminDealsOptionsDealTypesInner.from_json(json)
# print the JSON string representation of the object
print(AdminDealsOptionsDealTypesInner.to_json())

# convert the object into a dict
admin_deals_options_deal_types_inner_dict = admin_deals_options_deal_types_inner_instance.to_dict()
# create an instance of AdminDealsOptionsDealTypesInner from a dict
admin_deals_options_deal_types_inner_from_dict = AdminDealsOptionsDealTypesInner.from_dict(admin_deals_options_deal_types_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


