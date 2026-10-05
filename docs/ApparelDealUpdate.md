# ApparelDealUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cash_annual_avg** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**prod_allot_annual_avg** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**min_purchase_obl** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**signing_bonus** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**contingent_bonus** | **bool** |  | [optional] 
**sports** | [**List[ApparelDealUpdateSportsInner]**](ApparelDealUpdateSportsInner.md) | Sport IDs or case-insensitive display names; an empty array clears all sports. | [optional] 

## Example

```python
from winthrop_client_python.models.apparel_deal_update import ApparelDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApparelDealUpdate from a JSON string
apparel_deal_update_instance = ApparelDealUpdate.from_json(json)
# print the JSON string representation of the object
print(ApparelDealUpdate.to_json())

# convert the object into a dict
apparel_deal_update_dict = apparel_deal_update_instance.to_dict()
# create an instance of ApparelDealUpdate from a dict
apparel_deal_update_from_dict = ApparelDealUpdate.from_dict(apparel_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


