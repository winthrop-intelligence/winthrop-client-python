# DealUpdatePartner

Who the money goes to. One of the three partners; null or a blank (empty or whitespace-only) string clears it. Any other value is refused with 422 `deal_detail.partner`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from winthrop_client_python.models.deal_update_partner import DealUpdatePartner

# TODO update the JSON string below
json = "{}"
# create an instance of DealUpdatePartner from a JSON string
deal_update_partner_instance = DealUpdatePartner.from_json(json)
# print the JSON string representation of the object
print(DealUpdatePartner.to_json())

# convert the object into a dict
deal_update_partner_dict = deal_update_partner_instance.to_dict()
# create an instance of DealUpdatePartner from a dict
deal_update_partner_from_dict = DealUpdatePartner.from_dict(deal_update_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


