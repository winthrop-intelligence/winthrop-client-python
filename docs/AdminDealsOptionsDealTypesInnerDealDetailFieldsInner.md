# AdminDealsOptionsDealTypesInnerDealDetailFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**options** | **List[str]** |  | [optional] 
**applies_to** | **str** | Travel only (WINAD-10740). The travel_subtype this column belongs to; the form shows only the chosen subtype&#39;s columns. Absent for travel_subtype itself and every other deal type. | [optional] 
**help** | **str** |  | [optional] 

## Example

```python
from winthrop_client_python.models.admin_deals_options_deal_types_inner_deal_detail_fields_inner import AdminDealsOptionsDealTypesInnerDealDetailFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdminDealsOptionsDealTypesInnerDealDetailFieldsInner from a JSON string
admin_deals_options_deal_types_inner_deal_detail_fields_inner_instance = AdminDealsOptionsDealTypesInnerDealDetailFieldsInner.from_json(json)
# print the JSON string representation of the object
print(AdminDealsOptionsDealTypesInnerDealDetailFieldsInner.to_json())

# convert the object into a dict
admin_deals_options_deal_types_inner_deal_detail_fields_inner_dict = admin_deals_options_deal_types_inner_deal_detail_fields_inner_instance.to_dict()
# create an instance of AdminDealsOptionsDealTypesInnerDealDetailFieldsInner from a dict
admin_deals_options_deal_types_inner_deal_detail_fields_inner_from_dict = AdminDealsOptionsDealTypesInnerDealDetailFieldsInner.from_dict(admin_deals_options_deal_types_inner_deal_detail_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


