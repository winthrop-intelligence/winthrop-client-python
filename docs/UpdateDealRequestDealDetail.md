# UpdateDealRequestDealDetail

Fields must belong to the existing deal type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_annual_avg** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**prod_allot_annual_avg** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**min_purchase_obl** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**signing_bonus** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**sports** | [**List[ApparelDealUpdateSportsInner]**](ApparelDealUpdateSportsInner.md) | Sport IDs or case-insensitive display names; an empty array clears all sports. | [optional] 
**grf** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**bha** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**additional_rev** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**rev_share_percent** | [**MultimediaDealUpdateRevSharePercent**](MultimediaDealUpdateRevSharePercent.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.update_deal_request_deal_detail import UpdateDealRequestDealDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDealRequestDealDetail from a JSON string
update_deal_request_deal_detail_instance = UpdateDealRequestDealDetail.from_json(json)
# print the JSON string representation of the object
print(UpdateDealRequestDealDetail.to_json())

# convert the object into a dict
update_deal_request_deal_detail_dict = update_deal_request_deal_detail_instance.to_dict()
# create an instance of UpdateDealRequestDealDetail from a dict
update_deal_request_deal_detail_from_dict = UpdateDealRequestDealDetail.from_dict(update_deal_request_deal_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


