# ConcessionDealUpdate

Concessions deals (WINAD-10685).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_guar** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**annual_guar** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**partner** | [**DealUpdatePartner**](DealUpdatePartner.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.concession_deal_update import ConcessionDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ConcessionDealUpdate from a JSON string
concession_deal_update_instance = ConcessionDealUpdate.from_json(json)
# print the JSON string representation of the object
print(ConcessionDealUpdate.to_json())

# convert the object into a dict
concession_deal_update_dict = concession_deal_update_instance.to_dict()
# create an instance of ConcessionDealUpdate from a dict
concession_deal_update_from_dict = ConcessionDealUpdate.from_dict(concession_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


