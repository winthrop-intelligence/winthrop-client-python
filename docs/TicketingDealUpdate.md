# TicketingDealUpdate

Ticketing deals (WINAD-10685).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**maintenance** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 
**acct_mgr** | [**DealUpdateAmount**](DealUpdateAmount.md) |  | [optional] 

## Example

```python
from winthrop_client_python.models.ticketing_deal_update import TicketingDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TicketingDealUpdate from a JSON string
ticketing_deal_update_instance = TicketingDealUpdate.from_json(json)
# print the JSON string representation of the object
print(TicketingDealUpdate.to_json())

# convert the object into a dict
ticketing_deal_update_dict = ticketing_deal_update_instance.to_dict()
# create an instance of TicketingDealUpdate from a dict
ticketing_deal_update_from_dict = TicketingDealUpdate.from_dict(ticketing_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


