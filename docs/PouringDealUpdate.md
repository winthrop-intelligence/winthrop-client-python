# PouringDealUpdate

Pouring Rights deals (WINAD-10685). The guarantee is srf. Pouring has no total_guar or annual_guar and does NOT accept them, unlike Concessions; sending either is refused with 422. This is deliberate (pending confirmation from the ticket owner that srf is the intended Pouring guarantee).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**srf** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**avg_annual_prod** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**sla** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**signing_bonus** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**partner** | [**DealUpdatePartner**](DealUpdatePartner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.pouring_deal_update import PouringDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PouringDealUpdate from a JSON string
pouring_deal_update_instance = PouringDealUpdate.from_json(json)
# print the JSON string representation of the object
print(PouringDealUpdate.to_json())

# convert the object into a dict
pouring_deal_update_dict = pouring_deal_update_instance.to_dict()
# create an instance of PouringDealUpdate from a dict
pouring_deal_update_from_dict = PouringDealUpdate.from_dict(pouring_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


