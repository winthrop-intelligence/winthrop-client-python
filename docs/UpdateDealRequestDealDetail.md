# UpdateDealRequestDealDetail

Fields must belong to the existing deal type (see the schema of that type). Money fields take at most two decimals up to 999,999,999.99; percent fields 0 through 100.

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
**total_guar** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**annual_guar** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**partner** | [**DealUpdatePartner**](DealUpdatePartner.md) |  | [optional] 
**srf** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**avg_annual_prod** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**sla** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**license** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**maintenance** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**acct_mgr** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**total_rev_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**new_rev_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**renewal_rev_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**annual_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**threshold_1** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_1** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_2** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_2** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_3** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_3** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_4** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_4** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_5** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_5** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**threshold_6** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**alloc_percent_6** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**guaranteed_amt_year_one** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**capital_improvement** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**annual_host_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 

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


