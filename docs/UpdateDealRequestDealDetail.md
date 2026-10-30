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
**sports** | [**List[ApparelDealUpdateSportsInner]**](ApparelDealUpdateSportsInner.md) | Teams covered. Sport IDs or case-insensitive display names; an empty array clears all sports. Leave empty and set all_sports for department-wide deals. | [optional] 
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
**position_id** | **int** | Id of an existing position (the role being filled); anything else is refused with 422 &#x60;deal_detail.position_id&#x60;. | [optional] 
**search_scope** | **str** |  | [optional] 
**search_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**fee_basis** | **str** |  | [optional] 
**fee_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**guarantee_months** | [**DealUpdateMonths**](DealUpdateMonths.md) |  | [optional] 
**expense_terms** | **str** |  | [optional] 
**annual_retainer** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**products** | **str** | Vendor products, modules or packages bought, e.g. \&quot;Hub, ARMS, INFLCR\&quot;. Blank clears. | [optional] 
**all_sports** | **bool** | True only when the contract says department-wide or all teams. Null restores not stated. | [optional] 
**final_year_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**implementation_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**travel_subtype** | **str** | Kind of travel deal. Required when the detail is saved. | [optional] 
**management_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**agent_ticket_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**included_transactions** | [**DealUpdateCount**](DealUpdateCount.md) |  | [optional] 
**onsite_agents** | [**DealUpdateOnsiteAgents**](DealUpdateOnsiteAgents.md) |  | [optional] 
**after_hours_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**rate_per_mile** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**daily_rate** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**daily_rate_rule** | **str** | Bus Charter. How the daily rate is billed. Null clears. | [optional] 
**driver_overnight** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**price_per_round_trip** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**aircraft** | **str** | Air Charter. Aircraft type, e.g. A320. Blank clears. | [optional] 
**round_trips** | [**DealUpdateCount**](DealUpdateCount.md) |  | [optional] 

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


