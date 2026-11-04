# OutTicketingDealUpdate

Outsourced Ticketing deals (WINAD-10685).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rev_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**new_rev_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**renewal_rev_percent** | [**DealUpdatePercent**](DealUpdatePercent.md) |  | [optional] 
**annual_fee** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.out_ticketing_deal_update import OutTicketingDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of OutTicketingDealUpdate from a JSON string
out_ticketing_deal_update_instance = OutTicketingDealUpdate.from_json(json)
# print the JSON string representation of the object
print(OutTicketingDealUpdate.to_json())

# convert the object into a dict
out_ticketing_deal_update_dict = out_ticketing_deal_update_instance.to_dict()
# create an instance of OutTicketingDealUpdate from a dict
out_ticketing_deal_update_from_dict = OutTicketingDealUpdate.from_dict(out_ticketing_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


