# UpdateDealRequestDeal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_at** | **str** | ISO8601 date or datetime; null clears the start date. Date only, or datetime with T or space separator, optional seconds and fractional seconds, and optional Z or ±HH:MM/±HHMM offset. Time and offset hours must be 00-23; minutes and seconds must be 00-59. Offsets are honored. | [optional] 
**end_at** | **str** | ISO8601 date or datetime; cannot be null. Date only, or datetime with T or space separator, optional seconds and fractional seconds, and optional Z or ±HH:MM/±HHMM offset. Time and offset hours must be 00-23; minutes and seconds must be 00-59. Offsets are honored. | [optional] 
**autorenew** | **bool** |  | [optional] 
**verified** | **bool** | True requires a linked raw contract. | [optional] 

## Example

```python
from winthrop_client_python.models.update_deal_request_deal import UpdateDealRequestDeal

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDealRequestDeal from a JSON string
update_deal_request_deal_instance = UpdateDealRequestDeal.from_json(json)
# print the JSON string representation of the object
print(UpdateDealRequestDeal.to_json())

# convert the object into a dict
update_deal_request_deal_dict = update_deal_request_deal_instance.to_dict()
# create an instance of UpdateDealRequestDeal from a dict
update_deal_request_deal_from_dict = UpdateDealRequestDeal.from_dict(update_deal_request_deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


