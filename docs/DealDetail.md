# DealDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**grf** | **float** |  | [optional] 
**bha** | **float** |  | [optional] 
**rev_share_percent** | **float** |  | [optional] 
**signing_bonus** | **float** |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**additional_rev** | **float** |  | [optional] 
**cash_annual_avg** | **float** |  | [optional] 
**min_purchase_obl** | **float** |  | [optional] 
**prod_allot_annual_avg** | **float** |  | [optional] 
**srf** | **float** |  | [optional] 
**avg_annual_prod** | **float** |  | [optional] 
**sla** | **float** |  | [optional] 
**partner** | **str** |  | [optional] 
**total_guar** | **float** |  | [optional] 
**annual_guar** | **float** |  | [optional] 
**license** | **float** |  | [optional] 
**maintenance** | **float** |  | [optional] 
**acct_mgr** | **float** |  | [optional] 
**total_rev_percent** | **float** |  | [optional] 
**new_rev_percent** | **float** |  | [optional] 
**renewal_rev_percent** | **float** |  | [optional] 
**annual_fee** | **float** |  | [optional] 
**annual_host_fee** | **float** |  | [optional] 
**guaranteed_amt_year_one** | **float** |  | [optional] 
**capital_improvement** | **float** |  | [optional] 
**threshold_1** | **float** |  | [optional] 
**alloc_percent_1** | **float** |  | [optional] 
**threshold_2** | **float** |  | [optional] 
**alloc_percent_2** | **float** |  | [optional] 
**threshold_3** | **float** |  | [optional] 
**alloc_percent_3** | **float** |  | [optional] 
**threshold_4** | **float** |  | [optional] 
**alloc_percent_4** | **float** |  | [optional] 
**threshold_5** | **float** |  | [optional] 
**alloc_percent_5** | **float** |  | [optional] 
**threshold_6** | **float** |  | [optional] 
**alloc_percent_6** | **float** |  | [optional] 
**sports** | **List[str]** |  | [optional] 

## Example

```python
from winthrop_client_python.models.deal_detail import DealDetail

# TODO update the JSON string below
json = "{}"
# create an instance of DealDetail from a JSON string
deal_detail_instance = DealDetail.from_json(json)
# print the JSON string representation of the object
print(DealDetail.to_json())

# convert the object into a dict
deal_detail_dict = deal_detail_instance.to_dict()
# create an instance of DealDetail from a dict
deal_detail_from_dict = DealDetail.from_dict(deal_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


