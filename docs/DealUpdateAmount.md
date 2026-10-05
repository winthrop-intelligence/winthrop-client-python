# DealUpdateAmount

Nonnegative decimal with at most two decimal places, or null to clear.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from winthrop_client_python.models.deal_update_amount import DealUpdateAmount

# TODO update the JSON string below
json = "{}"
# create an instance of DealUpdateAmount from a JSON string
deal_update_amount_instance = DealUpdateAmount.from_json(json)
# print the JSON string representation of the object
print(DealUpdateAmount.to_json())

# convert the object into a dict
deal_update_amount_dict = deal_update_amount_instance.to_dict()
# create an instance of DealUpdateAmount from a dict
deal_update_amount_from_dict = DealUpdateAmount.from_dict(deal_update_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


