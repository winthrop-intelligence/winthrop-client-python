# TravelDealUpdate

Travel deals (WINAD-10740). A Travel deal is one of three subtypes and each subtype has its own columns. Every field is optional and null means not stated (never 0); an empty string also clears the text fields (daily_rate_rule, aircraft) but is refused for numbers. travel_subtype is required (in the body, or already stored) whenever any other field is sent. A column that does not apply to the effective subtype (the one in the body, else the stored one) is refused with 422 naming the field and the subtype. Agency columns are management_fee, agent_ticket_fee, included_transactions, onsite_agents and after_hours_fee; Bus Charter columns are rate_per_mile, daily_rate, daily_rate_rule and driver_overnight; Air Charter columns are price_per_round_trip, aircraft and round_trips.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from winthrop_client_python.models.travel_deal_update import TravelDealUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of TravelDealUpdate from a JSON string
travel_deal_update_instance = TravelDealUpdate.from_json(json)
# print the JSON string representation of the object
print(TravelDealUpdate.to_json())

# convert the object into a dict
travel_deal_update_dict = travel_deal_update_instance.to_dict()
# create an instance of TravelDealUpdate from a dict
travel_deal_update_from_dict = TravelDealUpdate.from_dict(travel_deal_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


