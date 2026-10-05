# DealUpdateDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**grf** | **str** |  | [optional] 
**bha** | **str** |  | [optional] 
**rev_share_percent** | **str** |  | [optional] 
**signing_bonus** | **str** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**additional_rev** | **str** |  | [optional] 
**cash_annual_avg** | **str** |  | [optional] 
**min_purchase_obl** | **str** |  | [optional] 
**prod_allot_annual_avg** | **str** |  | [optional] 
**srf** | **str** |  | [optional] 
**avg_annual_prod** | **str** |  | [optional] 
**sla** | **str** |  | [optional] 
**partner** | **str** |  | [optional] 
**total_guar** | **str** |  | [optional] 
**annual_guar** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**maintenance** | **str** |  | [optional] 
**acct_mgr** | **str** |  | [optional] 
**total_rev_percent** | **str** |  | [optional] 
**new_rev_percent** | **str** |  | [optional] 
**renewal_rev_percent** | **str** |  | [optional] 
**annual_fee** | **str** |  | [optional] 
**annual_host_fee** | **str** |  | [optional] 
**guaranteed_amt_year_one** | **str** |  | [optional] 
**capital_improvement** | **str** |  | [optional] 
**threshold_1** | **str** |  | [optional] 
**alloc_percent_1** | **str** |  | [optional] 
**threshold_2** | **str** |  | [optional] 
**alloc_percent_2** | **str** |  | [optional] 
**threshold_3** | **str** |  | [optional] 
**alloc_percent_3** | **str** |  | [optional] 
**threshold_4** | **str** |  | [optional] 
**alloc_percent_4** | **str** |  | [optional] 
**threshold_5** | **str** |  | [optional] 
**alloc_percent_5** | **str** |  | [optional] 
**threshold_6** | **str** |  | [optional] 
**alloc_percent_6** | **str** |  | [optional] 
**sports** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_update_detail import DealUpdateDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DealUpdateDetail from a JSON string
deal_update_detail_instance = DealUpdateDetail.from_json(json)
# print the JSON string representation of the object
print(DealUpdateDetail.to_json())

# convert the object into a dict
deal_update_detail_dict = deal_update_detail_instance.to_dict()
# create an instance of DealUpdateDetail from a dict
deal_update_detail_from_dict = DealUpdateDetail.from_dict(deal_update_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


